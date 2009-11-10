# -*- coding: utf-8 -*-
#
# Copyright (C) 2009  Kouhei Sutou <kou@clear-code.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License version 2.1 as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

class InvalidHTTPTest < Test::Unit::TestCase
  include GroongaTestUtils
  include GroongaHTTPTestUtils

  def setup
    setup_server
  end

  def teardown
    teardown_server
  end

  def test_root
    response = get("/")
    pend("should implement 404") do
      assert_equal("404", response.code)
    end
  end

  def test_outside_html_outside_existent_inner_nonexistent
    relative_path = "../../Makefile.am"
    assert_true(File.exist?(File.join(@resource_dir, relative_path)))
    assert_false(File.exist?(File.join(@resource_dir,
                                       File.basename(relative_path))))

    response = get("/#{relative_path}")
    pend("should implement 404") do
      assert_equal("404", response.code)
    end
    assert_equal("", response.body)
  end

  def test_outside_html_with_invalid_utf8
    relative_path = "../../Makefile.am"
    assert_true(File.exist?(File.join(@resource_dir, relative_path)))
    assert_false(File.exist?(File.join(@resource_dir,
                                       File.basename(relative_path))))
    invalid_relative_path = relative_path.gsub(/\//, "\xC0\x2F")

    response = get("/#{invalid_relative_path}")
    pend("should implement 404") do
      assert_equal("404", response.code)
    end
    assert_equal("", response.body)
  end

  def test_symbolic_link
    relative_path = "../../Makefile.am"
    relative_symbolic_link_path = "link"
    path = File.join(@resource_dir, relative_symbolic_link_path)
    symbolic_link_path = File.join(@resource_dir, relative_symbolic_link_path)
    assert_false(File.exist?(symbolic_link_path))

    begin
      FileUtils.ln_s(relative_path, symbolic_link_path)
      assert_true(File.exist?(symbolic_link_path))
      assert_true(File.exist?(path))
      assert_equal(File.read(path), File.read(symbolic_link_path))

      response = get("/#{relative_symbolic_link_path}")
      pend("should implement 404") do
        assert_equal("404", response.code)
      end
      assert_equal("", response.body)
    ensure
      FileUtils.rm_f(symbolic_link_path)
    end
  end

  def test_not_start_with_slash
    response = get(".")
    assert_equal("400", response.code)
    assert_equal("Bad Request: Your request path doesn't start with '/'.",
                 response.body)
  end

  def test_long_path
    response = get("/0123456789" * 10000)
    pend("should implement 404") do
      assert_equal("404", response.code)
    end
  end

  def test_long_query
    options = {}
    100.times do |i|
      options["key#{i}"] = "value#{i}"
    end
    response = get(command_path("table_list", options))
    assert_equal("200", response.code)
    assert_equal([["id", "name", "path", "flags", "domain"]],
                 JSON.parse(response.body))
  end

  def test_short_method
    socket = TCPSocket.new(@address, @port)
    socket.print("G")
    socket.flush
    Timeout.timeout(1) do
      response = get(command_path("table_list"))
      assert_equal("200", response.code)
    end
  end
end
