class TestIndexMatch < QueryOptimizerTestCase
  def setup
    Groonga::Schema.define do |schema|
      schema.create_table("Logs") do |table|
        table.text("message")
      end

      schema.create_table("Terms",
                          :type => :patricia_trie,
                          :default_tokenizer => "TokenBigram",
                          :normalizer => "NormalizerAuto") do |table|
        table.index("Logs", "message")
      end
    end

    @logs = Groonga["Logs"]
    setup_expression(@logs)
  end

  def teardown
    teardown_expression
  end

  def test_only
    assert_equal(<<-DUMP, dump_plan("message @ 'Groonga'"))
[0]
  op:         <match>
  logical_op: <or>
  index:      <[#<column:index Terms.Logs_message range:Logs sources:[Logs.message] flags:POSITION>]>
  query:      <"Groonga">
  expr:       <0..2>
    DUMP
  end

  def test_with_arithmetic_operator
    assert_equal(<<-DUMP, dump_plan("message @ 'Groonga' && ((1 + 1) == 2)"))
[0]
  op:         <match>
  logical_op: <or>
  index:      <[#<column:index Terms.Logs_message range:Logs sources:[Logs.message] flags:POSITION>]>
  query:      <"Groonga">
  expr:       <0..2>
[1]
  op:         <equal>
  logical_op: <and>
  index:      <[]>
  query:      <2>
  expr:       <3..7>
    DUMP
  end

  def test_not
    assert_equal(<<-DUMP, dump_plan("!(message @ 'Groonga')"))
[0]
  op:         <call>
  logical_op: <or>
  args[0]:    <#<proc:function all_records arguments:[]>>
  expr:       <0..0>
[1]
  op:         <match>
  logical_op: <and_not>
  index:      <[#<column:index Terms.Logs_message range:Logs sources:[Logs.message] flags:POSITION>]>
  query:      <"Groonga">
  expr:       <0..2>
    DUMP
  end

  def test_not_and_normal
    assert_equal(<<-DUMP, dump_plan("!(message @ 'Groonga') && (message @ 'Rroonga')"))
[0]
  op:         <call>
  logical_op: <or>
  args[0]:    <#<proc:function all_records arguments:[]>>
  expr:       <0..0>
[1]
  op:         <match>
  logical_op: <and_not>
  index:      <[#<column:index Terms.Logs_message range:Logs sources:[Logs.message] flags:POSITION>]>
  query:      <"Groonga">
  expr:       <0..2>
[2]
  op:         <match>
  logical_op: <and>
  index:      <[#<column:index Terms.Logs_message range:Logs sources:[Logs.message] flags:POSITION>]>
  query:      <"Rroonga">
  expr:       <4..6>
    DUMP
  end

  def test_normal_and_not
    assert_equal(<<-DUMP, dump_plan("(message @ 'Rroonga') && !(message @ 'Groonga')"))
[0]
  op:         <match>
  logical_op: <or>
  index:      <[#<column:index Terms.Logs_message range:Logs sources:[Logs.message] flags:POSITION>]>
  query:      <"Rroonga">
  expr:       <0..2>
[1]
  op:         <match>
  logical_op: <and_not>
  index:      <[#<column:index Terms.Logs_message range:Logs sources:[Logs.message] flags:POSITION>]>
  query:      <"Groonga">
  expr:       <3..5>
    DUMP
  end

  def test_normal_and_not_not
    assert_equal(<<-DUMP, dump_plan("(message @ 'Rroonga') &! !(message @ 'Groonga')"))
[0]
  op:         <match>
  logical_op: <or>
  index:      <[#<column:index Terms.Logs_message range:Logs sources:[Logs.message] flags:POSITION>]>
  query:      <"Rroonga">
  expr:       <0..2>
[1]
  op:         <match>
  logical_op: <and>
  index:      <[#<column:index Terms.Logs_message range:Logs sources:[Logs.message] flags:POSITION>]>
  query:      <"Groonga">
  expr:       <3..5>
    DUMP
  end
end