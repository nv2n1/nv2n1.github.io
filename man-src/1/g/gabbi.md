---
title: "gabbi(1)"
name: "gabbi"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gabbi/"
---

<h2>NAME</h2>

 gabbi - Gabbi Documentation 

 Gabbi tests are expressed in YAML as a series of HTTP requests with their expected response: 

 <pre>
tests:
   - name: retrieve root
     GET: /
     status: 200
</pre> 

 This will trigger a <b>GET</b> request to <b>/</b> on the configured <b>host</b>. The test will pass if the response's status code is <b>200</b>.

<h2>TEST STRUCTURE</h2>

 

 The top-level <b>tests</b> category contains an ordered sequence of test declarations, each describing the expected response to a given request:

<h3>Metadata</h3>

 <center><table> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> Key </td><td> Description </td><td> Notes 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> <b>name</b> </td><td> The test's name. Must be unique within a file. </td><td> <b>required</b> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> <b>desc</b> </td><td> An arbitrary string describing the test. </td><td> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> <b>verbose</b> </td><td> If <b>True</b> or <b>all</b> (synonymous), prints a representation of the current request and response to <b>stdout</b>, including both headers and body. If set to <b>headers</b> or <b>body</b>, only the corresponding part of the request and response will be printed. If the output is a TTY, colors will be used. See <b>VerboseHttp</b> for details. </td><td> defaults to <b>False</b> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> <b>skip</b> </td><td> A string message which if set will cause the test to be skipped with the provided message. </td><td> defaults to <b>False</b> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> <b>xfail</b> </td><td> Determines whether to expect this test to fail. Note that the test will be run anyway. </td><td> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> </table></center> 

 Note: When tests are generated dynamically, the <b>TestCase</b> name will include the respective test's <b>name</b>, lowercased with spaces transformed to <b>_</b>. In at least some test runners this will allow you to select and filter on test name.

<h3>Request Parameters</h3>

 <center><table> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> Key </td><td> Description </td><td> Notes 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> any uppercase string </td><td> Any such key is considered an HTTP method, with the corresponding value expressing the URL. 

 This is a shortcut combining <b>method</b> and <b>url</b> into a single statement: 

 <pre>
GET: /index
</pre> 

 corresponds to: 

 <pre>
method: GET
url: /index
</pre> </td><td> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> <b>method</b> </td><td> The HTTP request method. </td><td> defaults to <b>GET</b> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> <b>url</b> </td><td> The URL to request. This can either be a full path (e.g. &quot;/index&quot;) or a fully qualified URL (i.e. including host and scheme, e.g. &quot;<i><a rel="nofollow" HREF="http://example.org/index">http://example.org/index</a></i>&quot;) â see <b>host</b> for details. </td><td> <b>required</b> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> <b>request_headers</b> </td><td> A dictionary of key-value pairs representing request header names and values. These will be added to the constructed request. </td><td> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> <b>query_parameters</b> </td><td> A dictionary of query parameters that will be added to the <b>url</b> as query string. If that URL already contains a set of query parameters, those wil be extended. See <b>example</b> for a demonstration of how the data is structured. </td><td> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> <b>data</b> </td><td> A representation to pass as the body of a request. Note that <b>content-type</b> in <b>request_headers</b> should also be set â see <i>Data</i> for details. </td><td> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> <b>redirects</b> </td><td> If <b>True</b>, redirects will automatically be followed. </td><td> defaults to <b>False</b> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> <b>ssl</b> </td><td> Determines whether the request uses SSL (i.e. HTTPS). Note that the <b>url</b>'s scheme takes precedence if present â see <b>host</b> for details. </td><td> defaults to <b>False</b> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> </table></center>

<h3>Response Expectations</h3>

 <center><table> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> Key </td><td> Description </td><td> Notes 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> <b>status</b> </td><td> The expected response status code. Multiple acceptable response codes may be provided, separated by <b>||</b> (e.g. <b>302 || 301</b> â note, however, that this indicates ambiguity, which is generally undesirable). </td><td> defaults to <b>200</b> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> <b>response_headers</b> </td><td> A dictionary of key-value pairs representing expected response header names and values. If a header's value is wrapped in <b>/.../</b>, it will be treated as a regular expression. </td><td> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> <b>response_forbidden_headers</b> </td><td> A list of headers which must <i>not</i> be present. </td><td> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> <b>response_strings</b> </td><td> A list of string fragments expected to be present in the response body. </td><td> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> <b>response_json_paths</b> </td><td> A dictionary of JSONPath rules paired with expected matches. Using this rule requires that the content being sent from the server is JSON (i.e. a content type of <b>application/json</b> or containing <b>+json</b>) 

 If the value is wrapped in <b>/.../</b> the result of the JSONPath query will be compared against the value as a regular expression. </td><td> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> <tr VALIGN=top><td> <b>poll</b> </td><td> A dictionary of two keys:
<dl>
<dt>&bull;
<dd> <b>count</b>: An integer stating the number of times to attempt this test before giving up.
<dt>&bull;
<dd> <b>delay</b>: A floating point number of seconds to delay between attempts. 

 This makes it possible to poll for a resource created via an asynchronous request. Use with caution. </td><td> 
</td></tr> <tr VALIGN=top><td COLSPAN=3><hr></td></tr> </table></center> 

 Note that many of these items allow <i>substitutions</i>. 

 Default values for a file's <b>tests</b> may be provided via the top-level <b>defaults</b> category. These take precedence over the global defaults (explained below). 

 For examples see <i>the gabbi tests</i>, <b>example</b> and the <i>gabbi-demo</i> tutorial.</dl>

<h2>FIXTURES</h2>

 

 The top-level <b>fixtures</b> category contains a sequence of named <b>fixtures</b>.

<h2>RESPONSE HANDLERS</h2>

 

 <b>response_*</b> keys are examples of Response Handlers. Custom handlers may be created by test authors for specific use cases. See <b>handlers</b> for more information.

<h2>SUBSTITUTION</h2>

 

 There are a number of magical variables that can be used to make reference to the state of a current test or the one just prior. These are replaced with real values during test processing. They are processed in the order given.
<dl>
<dt>&bull;
<dd> <b>$SCHEME</b>: The current scheme/protocol (usually <b>http</b> or <b>https</b>).
<dt>&bull;
<dd> <b>$NETLOC</b>: The host and potentially port of the request.
<dt>&bull;
<dd> <b>$ENVIRON['&lt;environment variable&gt;']</b>: The name of an environment variable. Its value will replace the magical variable. If the string value of the environment variable is <b>&quot;True&quot;</b> or <b>&quot;False&quot;</b> then the resulting value will be the corresponding boolean, not a string.
<dt>&bull;
<dd> <b>$COOKIE</b>: All the cookies set by any <b>Set-Cookie</b> headers in the prior response, including only the cookie key and value pairs and no metadata (e.g. <b>expires</b> or <b>domain</b>).
<dt>&bull;
<dd> <b>$LAST_URL</b>: The URL defined in the prior request, after substitutions have been made.
<dt>&bull;
<dd> <b>$LOCATION</b>: The location header returned in the prior response.
<dt>&bull;
<dd> <b>$HEADERS['&lt;header&gt;']</b>: The value of any header from the prior response.
<dt>&bull;
<dd> <b>$RESPONSE['&lt;json path&gt;']</b>: A JSONPath query into the prior response. See <b>jsonpath</b> for more on formatting. 

 Where a single-quote character, <b>'</b>, is shown above you may also use a double-quote character, <b>&quot;</b>, but in any given expression the same character must be used at both ends. 

 All of these variables may be used in all of the following fields:
<dt>&bull;
<dd> <b>url</b>
<dt>&bull;
<dd> <b>query_parameters</b>
<dt>&bull;
<dd> <b>data</b>
<dt>&bull;
<dd> <b>request_headers</b>
<dt>&bull;
<dd> <b>response_strings</b>
<dt>&bull;
<dd> <b>response_json_paths</b> (on the value side of the key value pair)
<dt>&bull;
<dd> <b>response_headers</b> (on the value side of the key value pair)
<dt>&bull;
<dd> <b>response_forbidden_headers</b> 

 With these variables it ought to be possible to traverse an API without any explicit statements about the URLs being used. If you need a replacement on a field that is not currently supported please raise an issue or provide a patch. 

 As all of these features needed to be tested in the development of gabbi itself, <i>the gabbi tests</i> are a good source of examples on how to use the functionality. See also <b>example</b> for a collection of examples and the <i>gabbi-demo</i> tutorial.</dl>

<h2>DATA</h2>

 

 The <b>data</b> key has some special handing to allow for a bit more flexibility when doing a <b>POST</b> or <b>PUT</b>. If the value is not a string (that is, it is a sequence or structure) it is treated as a data structure which is turned into a JSON string. If the value is a string that begins with <b>&lt;@</b> then the rest of the string is treated as the name of a file to be loaded from the same directory as the YAML file. If the value is an undecorated string, that's the value. 

 When reading from a file care should be taken to ensure that a reasonable content-type is set for the data as this will control if any encoding is done of the resulting string value. If it is text, json, xml or javascript it will be encoded to UTF-8. 

 To run gabbi tests with a test harness they must be generated in some fashion and then run. This is accomplished by a test loader. Initially gabbi only supported those test harnesses that supported the <b>load_tests</b> protocol in UnitTest. It now possible to also build and run tests with <i>pytest</i> with some limitations described below. 

 <b>NOTE:</b> It is also possible to run gabbi tests from the command line. See <b>runner</b>. 

 <b>WARNING:</b> If test are being run with a runner that supports concurrency (such as <b>testrepository</b>) it is critical that the test runner is informed of how to group the tests into their respective suites. The usual way to do this is to use a regular expression that groups based on the name of the yaml files. For example, when using <b>testrepository</b> the <b>.testr.conf</b> file needs an entry similar to the following: 

 <pre>
group_regex=gabbi\.suitemaker\.(test_[^_]+_[^_]+)
</pre>

<h2>UNITTEST STYLE LOADER</h2>

 

 To run the tests with a <b>load_tests</b> style loader a test file containing a <b>load_tests</b> method is required. That will look a bit like: 

 <pre>
&quot;&quot;&quot;A sample test module.&quot;&quot;&quot;
# For pathname munging
import os
# The module that build_tests comes from.
from gabbi import driver
# We need access to the WSGI application that hosts our service
from myapp import wsgiapp
# We're using fixtures in the YAML files, we need to know where to
# load them from.
from myapp.test import fixtures
# By convention the YAML files are put in a directory named
# &quot;gabbits&quot; that is in the same directory as the Python test file.
TESTS_DIR = 'gabbits'
def load_tests(loader, tests, pattern):
    &quot;&quot;&quot;Provide a TestSuite to the discovery process.&quot;&quot;&quot;
    test_dir = os.path.join(os.path.dirname(__file__), TESTS_DIR)
    # Pass &quot;require_ssl=True&quot; as an argument to force all tests
    # to use SSL in requests.
    return driver.build_tests(test_dir, loader,
                              intercept=wsgiapp.app,
                              fixture_module=fixtures)
</pre> 

 For details on the arguments available when building tests see <b>build_tests()</b>. 

 Once the test loader has been created, it needs to be run. There are <i>many</i> options. Which is appropriate depends very much on your environment. Here are some examples using <b>unittest</b> or <b>testtools</b> that require minimal knowledge to get started. 

 By file: 

 <pre>
python -m testtools.run -v test/test_loader.py
</pre> 

 By module: 

 <pre>
python -m testttols.run -v test.test_loader
python -m unittest -v test.test_loader
</pre> 

 Using test discovery to locate all tests in a directory tree: 

 <pre>
python -m testtools.run discover
python -m unittest discover test
</pre> 

 See the <i>source distribution</i> and <i>the tutorial repo</i> for more advanced options, including using <b>testrepository</b> and <b>subunit</b>.

<h2>PYTEST</h2>

 

 Since pytest does not support the <b>load_tests</b> system, a different way of generating tests is required. A test file must be created that calls <b>py_test_generator()</b> and yields the generated tests. That will look a bit like this: 

 <pre>
&quot;&quot;&quot;A sample pytest module.&quot;&quot;&quot;
# For pathname munging
import os
# The module that build_tests comes from.
from gabbi import driver
# We need access to the WSGI application that hosts our service
from myapp import wsgiapp
# We're using fixtures in the YAML files, we need to know where to
# load them from.
from myapp.test import fixtures
# By convention the YAML files are put in a directory named
# &quot;gabbits&quot; that is in the same directory as the Python test file.
TESTS_DIR = 'gabbits'
def test_gabbits():
    test_dir = os.path.join(os.path.dirname(__file__), TESTS_DIR)
    # Pass &quot;require_ssl=True&quot; as an argument to force all tests
    # to use SSL in requests.
    test_generator = driver.py_test_generator(
        test_dir, intercept=wsgiapp.app,
        fixture_module=fixtures)
    for test in test_generator:
        yield test
</pre> 

 This can then be run with the usual pytest commands. For example: 

 <pre>
py.test -svx pytest-example.py
</pre> 

 <b>WARNING:</b> In <b>pytest&gt;=3.0</b> yield tests are deprecated and using them will cause pytest to produce a warning. If you wish to ignore and hide these warnings add the <b>--disable-pytest-warnings</b> parameter to the invocation of <b>py.test</b> or use a version of pytest earlier than version <b>3.0</b>. A new way of creating gabbi tests that works more effectively with modern pytest is being developed. 

 What follows is a commented example of some tests in a single file demonstrating many of the <b>format</b> features. See <b>loader</b> for the Python needed to integrate with a testing harness. 

 <pre>
# Fixtures can be used to set any necessary configuration, such as a
# persistence layer, and establish sample data. They operate per
# file. They are context managers, each one wrapping the next in the
# sequence.
fixtures:
    - ConfigFixture
    - SampleDataFixture
# There is an included fixture named &quot;SkipAllFixture&quot; which can be
# used to declare that all the tests in the given file are to be
# skipped.
# Each test file can specify a set of defaults that will be used for
# every request. This is useful for always specifying a particular
# header or always requiring SSL. These values will be used on every
# test in the file unless overriden. Lists and dicts are merged one
# level deep, except for &quot;data&quot; which is copied verbatim whether it
# is a string, list or dict (it can be all three).
defaults:
    ssl: True
    request_headers:
        x-my-token: zoom
# The tests themselves are a list under a &quot;tests&quot; key. It's useful
# to use plenty of whitespace to help readability.
tests:
# Each request *must* have a name which is unique to the file. When it
# becomes a TestCase the name will be lowercased and spaces will
# become &quot;_&quot;. Use that generated name when limiting test runs.
    - name: a test for root
      desc: Some explanatory text that could be used by other tooling
# The URL can either be relative to a host specified elsewhere or
# be a fully qualified &quot;http&quot; or &quot;https&quot; URL. *You* are responsible
# for url-encoding the URL.
      url: /
# If no status or method are provided they default to &quot;200&quot; and
# &quot;GET&quot;.
# A single test can override settings in defaults (set above).
    - name: root without ssl redirects
      ssl: False
      url: /
      status: 302
# When evaluating response headers it is possible to use a regular
# expression to not have to test the whole value.
      response_headers:
          location: /https/
# By default redirects will not be followed. This can be changed.
    - name: follow root without ssl redirect
      ssl: False
      redirects: True
      url: /
      status: 200 # This is the response code after the redirect.
# URLs can express query parameters in two ways: either in the url
# value directly, or as query_parameters. If both are used then
# query_parameters are appended. In this example the resulting URL
# will be equivalient to
# /foo?section=news&amp;article=1&amp;article=2&amp;date=yesterday
# but not necessarily in that order.
    - name: create a url with parameters
      url: /foo?section=news
      query_parameters:
          article:
              - 1
              - 2
          date: yesterday
# Request headers can be used to declare media-type choices and
# experiment with authorization handling (amongst other things).
# Response headers allow evaluating headers in the response. These
# two together form the core value of gabbi.
    - name: test accept
      url: /resource
      request_headers:
          accept: application/json
      response_headers:
          content-type: /application/json/
# If a header must not be present in a response at all that can be
# expressed in a test as follows.
    - name: test forbidden headers
      url: /resource
      response_forbidden_headers:
          - x-special-header
# All of the above requests have defaulted to a &quot;GET&quot; method. When
# using &quot;POST&quot;, &quot;PUT&quot; or &quot;PATCH&quot;, the &quot;data&quot; key provides the
# request body.
    - name: post some text
      url: /text_repo
      method: POST
      request_headers:
          content-type: text/plain
      data: &quot;I'm storing this&quot;
      status: 201
# If the data is not a string, it will be transformed into JSON.
# You must supply an appropriate content-type request header.
    - name: post some json
      url: /json_repo
      method: POST
      request_headers:
          content-type: application/json
      data:
          name: smith
          abode: castle
      status: 201
# If the data is a string prepended with &quot;&lt;@&quot; the value will be
# treated as the name of a file in the same directory as the YAML
# file. Again, you must supply an appropriate content-type. If the
# content-type is one of several &quot;text-like&quot; types, the content will
# be assumed to be UTF-8 encoded.
    - name: post an image
      url: /image_repo
      method: POST
      request_headers:
          content-type: image/png
      data: &lt;@kittens.png
# A single request can be marked to be skipped.
    - name: patch an image
      skip: patching images not yet implemented
      url: /image_repo/12d96fb8-e78c-11e4-8c03-685b35afa334
      method: PATCH
# Or a single request can be marked that it is expected to fail.
    - name: check allow headers
      desc: the framework doesn't do allow yet
      xfail: True
      url: /post_only_url
      method: PUT
      status: 405
      response_headers:
          allow: POST
# The body of a response can be evaluated with response handlers.
# The most simple checks for a set of strings anywhere in the
# response. Note that the strings are members of a list.
    - name: check for css file
      url: /blog/posts/12
      response_strings:
          - normalize.css
# For JSON responses, JSONPath rules can be used.
    - name: post some json get back json
      url: /json_repo
      method: POST
      request_headers:
          content-type: application/json
      data:
          name: smith
          abode: castle
      status: 201
      response_json_paths:
          $.name: smith
          $.abode: castle
# Requests run in sequence. One test can make reference to the test
# immediately prior using some special variables.
# &quot;$LOCATION&quot; contains the &quot;location&quot; header in the previous
# response.
# &quot;$HEADERS&quot; is a pseudo dictionary containing all the headers of
# the previous response.
# &quot;$ENVIRON&quot; is a pseudo dictionary providing access to the current
# environment.
# &quot;$RESPONSE&quot; provides access to the JSON in the prior response, via
# JSONPath. See <a rel="nofollow" HREF="http://jsonpath-rw.readthedocs.io/">http://jsonpath-rw.readthedocs.io/</a> for
# jsonpath-rw formatting.
# $SCHEME and $NETLOC provide access to the current protocol and
# location (host and port).
    - name: get the thing we just posted
      url: $LOCATION
      request_headers:
          x-magic-exchange: $HEADERS['x-magic-exchange']
          x-token: $ENVIRON['OS_TOKEN']
      response_json_paths:
          $.name: $RESPONSE['$.name']
          $.abode: $RESPONSE['$.abode']
      response_headers:
          content-location: /$SCHEME://$NETLOC/
# For APIs where resource creation is asynchronous it can be
# necessary to poll for the resulting resource. First we create the
# resource in one test. The next test uses the &quot;poll&quot; key to loop
# with a delay for a set number of times.
    - name: create asynch
      url: /async_creator
      method: POST
      request_headers:
          content-type: application/json
      data:
          name: jones
          abode: bungalow
      status: 202
    - name: poll for created resource
      url: $LOCATION
      poll:
          count: 10 # try up to ten times
          delay: .5 # wait .5 seconds between each try
      response_json_paths:
          $.name: $RESPONSE['$.name']
          $.abode: $RESPONSE['$.abode']
</pre> 

 Gabbi supports JSONPath both for validating JSON response bodies and within <i>substitutions</i>. 

 JSONPath expressions are provided by <i>jsonpath_rw</i>, with <i>jsonpath_rw_ext</i> custom extensions to address common requirements:
<dl>
<dt>1.
<dd> Sorting via <b>sorted</b> and <b>[/property]</b>.
<dt>2.
<dd> Filtering via <b>[?property = value]</b>.
<dt>3.
<dd> Returning the respective length via <b>len</b>. 

 (These apply both to arrays and key-value pairs.) 

 Here is a JSONPath example demonstrating some of these features. Given JSON data as follows: 

 <pre>
{
    &quot;pets&quot;: [
        {&quot;type&quot;: &quot;cat&quot;, &quot;sound&quot;: &quot;meow&quot;},
        {&quot;type&quot;: &quot;dog&quot;, &quot;sound&quot;: &quot;woof&quot;}
    ]
}
</pre> 

 If the ordering of the list in <b>pets</b> is predictable and reliable it is relatively straightforward to test values: 

 <pre>
response_json_paths:
    # length of list is two
    $.pets.`len`: 2
    # sound of second item in list is woof
    $.pets[1].sound: woof
</pre> 

 If the ordering is <i>not</i> predictable additional effort is required: 

 <pre>
response_json_paths:
    # sort by type
    $.pets[/type][0].sound: meow
    # sort by type, reversed
    $.pets[\type][0].sound: woof
    # all the sounds
    $.pets[/type]..sound: ['meow', 'woof']
    # filter by type = dog
    $.pets[?type = &quot;dog&quot;].sound: woof
</pre> 

 If it is necessary to validate the entire JSON response use a JSONPath of <b>$</b>: 

 <pre>
response_json_paths:
    $:
        pets:
            - type: cat
              sound: meow
            - type: dog
              sound: woof
</pre> 

 This is not a technique that should be used frequently as it can lead to difficult to read tests and it also indicates that your gabbi tests are being used to test your serializers and data models, not just your API interactions. 

 There are more JSONPath examples in <b>example</b> and in the <i>jsonpath_rw</i> and <i>jsonpath_rw_ext</i> documentation. 

 The target host is the host on which the API to be tested can be found. Gabbi intends to preserve the flow and semantics of HTTP interactions as much as possible, and every HTTP request needs to be directed at a host of some form. Gabbi provides three ways to control this:
<dt>&bull;
<dd> Using <i>wsgi-intercept</i> to provide a fake socket and <b>WSGI</b> environment on an arbitrary host and port attached to a <b>WSGI</b> application (see <i>intercept examples</i>).
<dt>&bull;
<dd> Using fully qualified <b>url</b> values in the YAML defined tests (see <i>full examples</i>).
<dt>&bull;
<dd> Using a host and (optionally) port defined at test build time (see <i>live examples</i>). 

 The intercept and live methods are mutually exclusive per test builder, but either kind of test can freely intermix fully qualified URLs into the sequence of tests in a YAML file. 

 For test driven development and local tests the intercept style of testing lowers test requirements (no web server required) and is fast. Interception is performed as part of <b>fixtures</b> processing as the most deeply nested fixture. This allows any configuration or database setup to be performed prior to the WSGI application being created. 

 For the implementation of the above see <b>build_tests()</b>. 

 Each suite of tests is represented by a single YAML file, and may optionally use one or more fixtures to provide the necessary environment required by the tests in that file. 

 Fixtures are implemented as nested context managers. Subclasses of <b>GabbiFixture</b> must implement <b>start_fixture</b> and <b>stop_fixture</b> methods for creating and destroying, respectively, any resources managed by the fixture. While the subclass may choose to implement <b>__init__</b> it is important that no exceptions are thrown in that method, otherwise the stack of context managers will fail in unexpected ways. Instead initialization of real resources should happen in <b>start_fixture</b>. 

 At this time there is no mechanism for the individual tests to have any direct awareness of the fixtures. The fixtures exist, conceptually, on the server side of the API being tested. 

 Fixtures may do whatever is required by the testing environment, however there are two common scenarios:
<dt>&bull;
<dd> Establishing (and then resetting when a test suite has finished) any baseline configuration settings and persistence systems required for the tests.
<dt>&bull;
<dd> Creating sample data for use by the tests. 

 If a fixture raises <b>unittest.case.SkipTest</b> during <b>start_fixture</b> all the tests in the current file will be skipped. This makes it possible to skip the tests if some optional configuration (such as a particular type of database) is not available. 

 If an exception is raised while a fixture is being used, information about the exception will be stored on the fixture so that the <b>stop_fixture</b> method can decide if the exception should change how the fixture should clean up. The exception information can be found on <b>exc_type</b>, <b>exc_value</b> and <b>traceback</b> method attributes. 

 In some contexts (for example CI environments with a large number of tests being run in a broadly concurrent environment where output is logged to a single file) it can be important to capture and consolidate stray output that is produced during the tests and display it associated with an individual test. This can help debugging and avoids unusable output that is the result of multiple streams being interleaved. 

 Inner fixtures have been added to support this. These are fixtures more in line with the tradtional <b>unittest</b> concept of fixtures: a class on which <b>setUp</b> and <b>cleanUp</b> is automatically called. 

 <b>build_tests()</b> accepts a named parameter arguments of <b>inner_fixtures</b>. The value of that argument may be an ordered list of <i>fixtures.Fixture</i> classes that will be called when each individual test is set up. 

 An example fixture that could be useful is the <i>FakeLogger</i>. 

 <b>NOTE:</b> At this time <b>inner_fixtures</b> are not supported when using the pytest <b>loader</b>. 

 Content handlers are responsible for preparing request data and evaluating response data based on the content-type of the request and response. A content handler operates as follows:
<dt>&bull;
<dd> Structured YAML data provided via the <b>data</b> attribute is converted to a string or bytes sequence and used as request body.
<dt>&bull;
<dd> The response body (a string or sequence of bytes) is transformed into a content-type dependent structure and stored in an internal attribute named <b>response_data</b> that is:
<dt>&bull;
<dd> used when evaluating the response body
<dt>&bull;
<dd> used in <b>$RESPONSE[]</b> <i>substitutions</i> 

 By default, gabbi provides content handlers for JSON. In that content handler the <b>data</b> test key is converted from structured YAML into a JSON string. Response bodies are converted from a JSON string into a data structure in <b>response_data</b> that is used when evaluating <b>response_json_paths</b> entries in a test or doing JSONPath-based <b>$RESPONSE[]</b> substitutions. 

 Further content handlers can be added as extensions. Test authors may need these extensions for their own suites, or enterprising developers may wish to create and distribute extensions for others to use. 

 <b>NOTE:</b> One extension that is likely to be useful is a content handler that turns <b>data</b> into url-encoded form data suitable for POST and turns an HTML response into a DOM object.</dl>

<h2>EXTENSIONS</h2>

 

 Content handlers are an evolution of the response handler concept in earlier versions gabbi. To preserve backwards compatibility with existing response handlers, old style response handlers are still allowed, but new handlers should implement the content handler interface (described below). 

 Registering additional custom handlers is done by passing a subclass of <b>ContentHandler</b> to <b>build_tests()</b>: 

 <pre>
driver.build_tests(test_dir, loader, host=None,
                   intercept=simple_wsgi.SimpleWsgi,
                   content_handlers=[MyContentHandler])
</pre> 

 If pytest is being used: 

 <pre>
driver.py_test_generator(test_dir, intercept=simple_wsgi.SimpleWsgi,
                         content_handlers=[MyContenHandler])
</pre> 

 <b>WARNING:</b> When there are multiple handlers listed that accept the same content-type, the one that is earliest in the list will be used. 

 With <b>gabbi-run</b>, custom handlers can be loaded via the <b>--response-handler</b> option -- see <b>load_response_handlers()</b> for details. 

 <b>NOTE:</b> The use of the <b>--response-handler</b> argument is done to preserve backwards compatibility and avoid excessive arguments. Both types of handler may be passed to the argument.

<h3>Implementation Details</h3>

 

 Creating a content handler requires subclassing <b>ContentHandler</b> and implementing several methods. These methods are described below, but inspecting <b>JSONHandler</b> will be instructive in highlighting required arguments and techniques. 

 To provide a <b>response_&lt;something&gt;</b> response-body evaluator a subclass must define:
<dl>
<dt>&bull;
<dd> <b>test_key_suffix</b>: This, along with the prefix <b>response_</b>, forms the key used in the test structure. It is a class level string.
<dt>&bull;
<dd> <b>test_key_value</b>: The key's default value, either an empty list (<b>[]</b>) or empty dict (<b>{}</b>). It is a class level value.
<dt>&bull;
<dd> <b>action</b>: An instance method which tests the expected values against the HTTP response - it is invoked for each entry, with the parameters depending on the default value. The arguments to <b>action</b> are (in order):
<dt>&bull;
<dd> <b>self</b>: The current instance.
<dt>&bull;
<dd> <b>test</b>: The currently active <b>HTTPTestCase</b>
<dt>&bull;
<dd> <b>item</b>: The current entry if <b>test_key_value</b> is a list, otherwise the key half of the key/value pair at this entry.
<dt>&bull;
<dd> <b>value</b>: <b>None</b> if <b>test_key_value</b> is a list, otherwise the value half of the key/value pair at this entry. 

 To translate request or response bodies to or from structured data a subclass must define an <b>accepts</b> method. This should return <b>True</b> if this class is willing to translate the provided content-type. During request processing it is given the value of the content-type header that will be sent in the request. During response processing it is given the value of the content-type header of the response. This makes it possible to handle different request and response bodies in the same handler, if desired. For example a handler might accept <b>application/x-www-form-urlencoded</b> and <b>text/html</b>. 

 If <b>accepts</b> is defined two additional static methods should be defined:
<dt>&bull;
<dd> <b>dumps</b>: Turn structured Python data from the <b>data</b> key in a test into a string or byte stream.
<dt>&bull;
<dd> <b>loads</b>: Turn a string or byte stream in a response into a Python data structure. Gabbi will put this data on the <b>response_data</b> attribute on the test, where it can be used in the evaluations described above (in the <b>action</b> method) or in <b>$RESPONSE</b> handling. An example usage here would be to turn HTML into a DOM. 

 Finally if a <b>replacer</b> class method is defined, then when a <b>$RESPONSE</b> substitution is encountered, <b>replacer</b> will be passed the <b>response_data</b> of the prior test and the argument within the <b>$RESPONSE</b>. 

 Please see the <i>JSONHandler source</i> for additional detail. 

 If there is a running web service that needs to be tested and creating a test loader with <b>build_tests()</b> is either inconvenient or overkill it is possible to run YAML test files directly from the command line with the console-script <b>gabbi-run</b>. It accepts YAML on <b>stdin</b> or as multiple file arguments, and generates and runs tests and outputs a summary of the results. 

 The provided YAML may not use custom <b>fixtures</b> but otherwise uses the default <b>format</b>. <b>host</b> information is either expressed directly in the YAML file or provided on the command line: 

 <pre>
gabbi-run [host[:port]] &lt; /my/test.yaml
</pre> 

 or: 

 <pre>
gabbi-run <a rel="nofollow" HREF="http://host:port">http://host:port</a> &lt; /my/test.yaml
</pre> 

 To test with one or more files the following command syntax may be used: 

 <pre>
gabbi-run <a rel="nofollow" HREF="http://host:port">http://host:port</a> -- /my/test.yaml /my/other.yaml
</pre> 

 <b>NOTE:</b> The filename arguments must come after a <b>--</b> and all other arguments (host, port, prefix, failfast) must come before the <b>--</b>. 

 To facilitate using the same tests against the same application mounted in different locations in a WSGI server, a <b>prefix</b> may be provided as a second argument: 

 <pre>
gabbi-run host[:port] [prefix] &lt; /my/test.yaml
</pre> 

 or in the target URL: 

 <pre>
gabbi-run <a rel="nofollow" HREF="http://host:port/prefix">http://host:port/prefix</a> &lt; /my/test.yaml
</pre> 

 The value of prefix will be prepended to the path portion of URLs that are not fully qualified. 

 Anywhere host is used, if it is a raw IPV6 address it should be wrapped in <b>[</b> and <b>]</b>. 

 If <b>https</b> is used in the target, then the tests in the provided YAML will default to <b>ssl: True</b>. 

 If a <b>-x</b> or <b>--failfast</b> argument is provided then <b>gabbi-run</b> will exit after the first test failure. 

 These are informal release notes for gabbi since version 1.0.0, highlighting major features and changes. For more detail see the <i>commit logs</i> on GitHub.</dl>

<h2>1.27.0</h2>

 

 Allow <b>gabbi-run</b> to accept multiple filenames as command line arguments instead of reading tests from stdin.

<h2>1.26.0</h2>

 

 Switch from response handlers to <b>handlers</b> to allow more flexible processing of both response _and_ request bodies. 

 Add <i>inner fixtures</i> for per test fixtures, useful for output capturing.

<h2>1.25.0</h2>

 

 Allow the <b>test_loader_name</b> arg to <b>gabbi.driver.build_tests()</b> to override the prefix of the pretty printed name of generated tests.

<h2>1.24.0</h2>

 

 String values in JSONPath matches may be wrapped in <b>/.../`</b> to be treated as regular expressions.

<h2>1.23.0</h2>

 

 Better <b>documentation</b> of how to run gabbi in a concurrent environment. Improved handling of pytest fixtures and test counts.

<h2>1.22.0</h2>

 

 Add <b>url</b> to <b>gabbi.driver.build_tests()</b> to use instead of <b>host</b>, <b>port</b> and <b>prefix</b>.

<h2>1.21.0</h2>

 

 Add <b>require_ssl</b> to <b>gabbi.driver.build_tests()</b> to force use of SSL.

<h2>1.20.0</h2>

 

 Add <b>$COOKIE</b> <i>substitution</i>.

<h2>1.19.1</h2>

 

 Correctly support IPV6 hosts.

<h2>1.19.0</h2>

 

 Add <b>$LAST_URL</b> <i>substitution</i>.

<h2>1.17.0</h2>

 

 Introduce support for loading and running tests with pytest.

<h2>1.16.0</h2>

 

 Use urllib3 instead of httplib2 for driving HTTP requests.

<h2>1.13.0</h2>

 

 Add sorting and filtering to <b>jsonpath</b> handling.

<h2>1.11.0</h2>

 

 Add the <b>response_forbidden_headers</b> to <i>response expectations</i>.

<h2>1.7.0</h2>

 

 Instead of: 

 <pre>
tests:
- name: a simple get
  url: /some/path
  method: get
</pre> 

 1.7.0 also makes it possible to: 

 <pre>
tests:
- name: a simple get
  GET: /some/path
</pre> 

 Any upper case key is treated as a method.

<h2>1.4.0 AND 1.5.0</h2>

 

 Enhanced flexibility and colorization when setting tests to be <i>verbose</i>.

<h2>1.3.0</h2>

 

 Adds the <b>query_parameters</b> key to <i>request parameters</i>.

<h2>1.2.0</h2>

 

 The start of improvements and extensions to <b>jsonpath</b> handling. In this case the addition of the <b>len</b> function.

<h2>1.1.0</h2>

 

 Vastly improved output and behavior in <b>gabbi-run</b>.

<h2>1.0.0</h2>

 

 Version 1 was the first release with a commitment to a stable <b>format</b>. Since then new fields have been added but have not been taken away. 

 The following people have contributed code to gabbi. Thanks to them. Thanks also to all the people who have made gabbi better by reporting <i>issues</i> and their successes and failures with using gabbi.
<dl>
<dt>&bull;
<dd> Chris Dent
<dt>&bull;
<dd> FND
<dt>&bull;
<dd> Mehdi Abaakouk
<dt>&bull;
<dd> Jason Myers
<dt>&bull;
<dd> Kim Raymoure
<dt>&bull;
<dd> Michael McCune
<dt>&bull;
<dd> Imran Hayder
<dt>&bull;
<dd> Julien Danjou
<dt>&bull;
<dd> Danek Duvall
<dt>&bull;
<dd> Marc Abramowitz 

 <b>NOTE:</b> This section provides a collection of questions with answers that don't otherwise fit in the rest of the documentation. If something is missing, please create an <i>issue</i>. 

 As this document grows it will gain a more refined structure.</dl>

<h2>GENERAL</h2>

<h3>Is gabbi only for testing Python-based APIs?</h3>

 

 No, you can use <b>gabbi-run</b> to test an HTTP service built in any programming language.

<h2>WORKAROUNDS</h2>

<h3>pytest produces warnings about yield tests. Can I make them stop?</h3>

 

 Yes, run as <b>py.test --disable-pytest-warnings</b> to quiet the warnings. Or use a version of pytest less than <b>3.0</b>. For more details see <i>pytest</i>.

<h2>TESTING STYLE</h2>

<h3>Can I have variables in my YAML file?</h3>

 

 Gabbi provides the <b>$ENVIRON</b> <i>substitution</i> which can operate a bit like variables that are set elsewhere and then used in the tests defined by the YAML. 

 If you find it necessary to have variables within a single YAML file you take advantage of YAML <i>alias nodes</i> list this: 

 <pre>
vars:
  - &amp;uuid_1 5613AABF-BAED-4BBA-887A-252B2D3543F8
tests:
- name: send a uuid to a post
  POST: /resource
  request_headers:
    content-type: application/json
  data:
    uuid: *uuid_1
</pre> 

 You can alias all sorts of nodes, not just single items. Be aware that the replacement of an alias node happens while the YAML is being loaded, before gabbi does any processing.

<h3>How many tests should be put in one YAML file?</h3>

 

 For the sake of readability it is best to keep each YAML file relatively short. Since each YAML file represents a sequence of requests, it usually makes sense to create a new file when a test is not dependent on any before it. 

 It's tempting to put all the tests for any resource or URL in the same file, but this eventually leads to files that are too long and are thus difficult to read.

<h2>CASE MODULE</h2>

 

 A single HTTP request represented as a subclass of <b>testtools.TestCase</b> 

 The test case encapsulates the request headers and body and expected response headers and body. When the test is run an HTTP request is made using urllib3. Assertions are made against the reponse.
<dl>
<dt><b>class gabbi.case.HTTPTestCase(*args, **kwargs)</b>
<dd> Bases: <b>testtools.testcase.TestCase</b> 

 Encapsulate a single HTTP request as a TestCase. 

 If the test is a member of a sequence of requests, ensure that prior tests are run. 

 To keep the test harness happy we need to make sure the setUp and tearDown are only run once.
<dt><b>assert_in_or_print_output(expected, iterable)</b>
<dd> Assert the iterable contains expected or print some output. 

 If the output is long, it is limited by either GABBI_MAX_CHARS_OUTPUT in the environment or the MAX_CHARS_OUTPUT constant.
<dt><b>base_test = {'status': '200', 'xfail': False, 'redirects': False, 'verbose': False, 'query_parameters': {}, 'url': '', 'skip': '', 'name': '', 'ssl': False, 'request_headers': {}, 'poll': {}, 'data': '', 'method': 'GET', 'desc': ''}</b>
<dd>
<dt><b>get_content_handler(content_type)</b>
<dd> Determine the content handler for this media type.
<dt><b>replace_template(message)</b>
<dd> Replace magic strings in message.
<dt><b>run(result=None)</b>
<dd> Store the current result handler on this test.
<dt><b>setUp()</b>
<dd>
<dt><b>tearDown()</b>
<dd>
<dt><b>test_request()</b>
<dd> Run this request if it has not yet run. 

 If there is a prior test in the sequence, run it first.
<dt><b>gabbi.case.potentialFailure(func)</b>
<dd> Decorate a test method that is expected to fail if 'xfail' is true.</dl>

<h2>DRIVER MODULE</h2>

 

 Generate HTTP tests from YAML files 

 Each HTTP request is its own TestCase and can be requested to be run in isolation from other tests. If it is a member of a sequence of requests, prior requests will be run. 

 A sequence is represented by an ordered list in a single YAML file. 

 Each sequence becomes a TestSuite. 

 An entire directory of YAML files is a TestSuite of TestSuites.
<dl>
<dt><b>gabbi.driver.build_tests(path, loader, host=None, port=8001, intercept=None, test_loader_name=None, fixture_module=None, response_handlers=None, content_handlers=None, prefix='', require_ssl=False, url=None, inner_fixtures=None)</b>
<dd> Read YAML files from a directory to create tests. 

 Each YAML file represents an ordered sequence of HTTP requests.
<dt><b>Parameters</b>
<dd>
<dt>&bull;
<dd> <b>path</b> -- The directory where yaml files are located.
<dt>&bull;
<dd> <b>loader</b> -- The TestLoader.
<dt>&bull;
<dd> <b>host</b> -- The host to test against. Do not use with <b>intercept</b>.
<dt>&bull;
<dd> <b>port</b> -- The port to test against. Used with <b>host</b>.
<dt>&bull;
<dd> <b>intercept</b> -- WSGI app factory for wsgi-intercept.
<dt>&bull;
<dd> <b>test_loader_name</b> -- Base name for test classes. Use this to align the naming of the tests with other tests in a system.
<dt>&bull;
<dd> <b>fixture_module</b> -- Python module containing fixture classes.
<dt>&bull;
<dd> <b>response_handers</b> -- <b>ResponseHandler</b> classes.
<dt>&bull;
<dd> <b>content_handlers</b> (<i>List of ContentHandler classes.</i>) -- ContentHandler classes.
<dt>&bull;
<dd> <b>prefix</b> -- A URL prefix for all URLs that are not fully qualified.
<dt>&bull;
<dd> <b>url</b> -- A full URL to test against. Replaces host, port and prefix.
<dt>&bull;
<dd> <b>require_ssl</b> -- If <b>True</b>, make all tests default to using SSL.
<dt>&bull;
<dd> <b>inner_fixtures</b> (<i>List of fixtures.Fixture classes.</i>) -- A list of <b>Fixtures</b> to use with each individual test request.
<dt><b>Return type</b>
<dd> TestSuite containing multiple TestSuites (one for each YAML file).
<dt><b>gabbi.driver.py_test_generator(test_dir, host=None, port=8001, intercept=None, prefix=None, test_loader_name=None, fixture_module=None, response_handlers=None, content_handlers=None, require_ssl=False, url=None)</b>
<dd> Generate tests cases for py.test 

 This uses build_tests to create TestCases and then yields them in a way that pytest can handle.
<dt><b>gabbi.driver.test_suite_from_yaml(loader, test_base_name, test_yaml, test_directory, host, port, fixture_module, intercept, prefix='')</b>
<dd> Legacy wrapper retained for backwards compatibility.</dl>

<h2>SUITEMAKER MODULE</h2>

 

 The code that creates a suite of tests. 

 The key piece of code is <b>test_suite_from_dict()</b>. It produces a <b>gabbi.suite.GabbiSuite</b> containing one or more <b>gabbi.case.HTTPTestCase</b>.
<dl>
<dt><b>class gabbi.suitemaker.TestBuilder</b>
<dd> Bases: <b>type</b> 

 Metaclass to munge a dynamically created test.
<dt><b>required_attributes = {'has_run': False}</b>
<dd>
<dt><b>class gabbi.suitemaker.TestMaker(test_base_name, test_defaults, test_directory, fixture_classes, loader, host, port, intercept, prefix, response_handlers, content_handlers, test_loader_name=None, inner_fixtures=None)</b>
<dd> Bases: <b>object</b> 

 A class for encapsulating test invariants. 

 All of the tests in a single gabbi file have invariants which are provided when creating each HTTPTestCase. It is not useful to pass these around when making each test case. So they are wrapped in this class which then has make_one_test called multiple times to generate all the tests in the suite.
<dt><b>make_one_test(test_dict, prior_test)</b>
<dd> Create one single HTTPTestCase. 

 The returned HTTPTestCase is added to the TestSuite currently being built (one per YAML file).
<dt><b>gabbi.suitemaker.test_suite_from_dict(loader, test_base_name, suite_dict, test_directory, host, port, fixture_module, intercept, prefix='', handlers=None, test_loader_name=None, inner_fixtures=None)</b>
<dd> Generate a GabbiSuite from a dict represent a list of tests. 

 The dict takes the form:
<dt><b>Parameters</b>
<dd>
<dt>&bull;
<dd> <b>fixtures</b> -- An optional list of fixture classes that this suite can use.
<dt>&bull;
<dd> <b>defaults</b> -- An optional dictionary of default values to be used in each test.
<dt>&bull;
<dd> <b>tests</b> -- A list of individual tests, themselves each being a dictionary. See <b>gabbi.case.BASE_TEST</b>.
<dt><b>gabbi.suitemaker.test_update(orig_dict, new_dict)</b>
<dd> Modify test in place to update with new data.</dl>

<h2>FIXTURE MODULE</h2>

 

 Manage fixtures for gabbi at the test suite level.
<dl>
<dt><b>class gabbi.fixture.GabbiFixture</b>
<dd> Bases: <b>object</b> 

 A context manager that operates as a fixture. 

 Subclasses must implement <b>start_fixture</b> and <b>stop_fixture</b>, each of which contain the logic for stopping and starting whatever the fixture is. What a fixture is is left as an exercise for the implementor. 

 These context managers will be nested so any actual work needs to happen in <b>start_fixture</b> and <b>stop_fixture</b> and not in <b>__init__</b>. Otherwise exception handling will not work properly.
<dt><b>start_fixture()</b>
<dd> Implement the actual workings of starting the fixture here.
<dt><b>stop_fixture()</b>
<dd> Implement the actual workings of stopping the fixture here.
<dt><b>exception gabbi.fixture.GabbiFixtureError</b>
<dd> Bases: <b>exceptions.Exception</b> 

 Generic exception for GabbiFixture.
<dt><b>class gabbi.fixture.SkipAllFixture</b>
<dd> Bases: <b>gabbi.fixture.GabbiFixture</b> 

 A fixture that skips all the tests in the current suite.
<dt><b>start_fixture()</b>
<dd>
<dt><b>gabbi.fixture.nest(*args, **kwds)</b>
<dd> Nest a series of fixtures. 

 This is duplicated from <b>nested</b> in the stdlib, which has been deprecated because of issues with how exceptions are difficult to handle during <b>__init__</b>. Gabbi needs to nest an unknown number of fixtures dynamically, so the <b>with</b> syntax that replaces <b>nested</b> will not work.</dl>

<h2>HANDLERS MODULE</h2>

 

 Package for response and content handlers that process the body of a response in various ways.

<h3><b>handlers.base</b> Module</h3>

 

 Base classes for response and content handlers.
<dl>
<dt><b>class gabbi.handlers.base.ContentHandler</b>
<dd> Bases: <b>gabbi.handlers.base.ResponseHandler</b> 

 A subclass of ResponseHandlers that adds content handling.
<dt><b>static accepts(content_type)</b>
<dd> Return True if this handler can handler this type.
<dt><b>static dumps(data, pretty=False)</b>
<dd> Return structured data as a string. 

 If pretty is true, prettify.
<dt><b>classmethod gen_replacer(test)</b>
<dd> Return a function which does RESPONSE replacing.
<dt><b>static loads(data)</b>
<dd> Create structured (Python) data from a stream.
<dt><b>classmethod replacer(response_data, path)</b>
<dd> Return the string the is replacing RESPONSE.
<dt><b>class gabbi.handlers.base.ResponseHandler</b>
<dd> Bases: <b>object</b> 

 Add functionality for making assertions about an HTTP response. 

 A subclass may implement two methods: <b>action</b> and <b>preprocess</b>. 

 <b>preprocess</b> takes one argument, the <b>TestCase</b>. It is called exactly once for each test before looping across the assertions. It is used, rarely, to copy the <b>test.output</b> into a useful form (such as a parsed DOM). 

 <b>action</b> takes two or three arguments. If <b>test_key_value</b> is a list <b>action</b> is called with the test case and a single list item. If <b>test_key_value</b> is a dict then <b>action</b> is called with the test case and a key and value pair.
<dt><b>action(test, item, value=None)</b>
<dd> Test an individual entry for this response handler. 

 If the entry is a key value pair the key is in item and the value in value. Otherwise the entry is considered a single item from a list.
<dt><b>preprocess(test)</b>
<dd> Do any pre-single-test preprocessing.
<dt><b>test_key_suffix = ''</b>
<dd>
<dt><b>test_key_value = []</b>
<dd></dl>

<h3><b>handlers.core</b> Module</h3>

 

 Core response handlers.
<dl>
<dt><b>class gabbi.handlers.core.ForbiddenHeadersResponseHandler</b>
<dd> Bases: <b>gabbi.handlers.base.ResponseHandler</b> 

 Test that listed headers are not in the response.
<dt><b>action(test, forbidden, value=None)</b>
<dd>
<dt><b>test_key_suffix = 'forbidden_headers'</b>
<dd>
<dt><b>test_key_value = []</b>
<dd>
<dt><b>class gabbi.handlers.core.HeadersResponseHandler</b>
<dd> Bases: <b>gabbi.handlers.base.ResponseHandler</b> 

 Compare expected headers with actual headers. 

 If a header value is wrapped in <b>/</b> it is treated as a raw regular expression. 

 Headers values are always treated as strings.
<dt><b>action(test, header, value=None)</b>
<dd>
<dt><b>test_key_suffix = 'headers'</b>
<dd>
<dt><b>test_key_value = {}</b>
<dd>
<dt><b>class gabbi.handlers.core.StringResponseHandler</b>
<dd> Bases: <b>gabbi.handlers.base.ResponseHandler</b> 

 Test for matching strings in the the response body.
<dt><b>action(test, expected, value=None)</b>
<dd>
<dt><b>test_key_suffix = 'strings'</b>
<dd>
<dt><b>test_key_value = []</b>
<dd></dl>

<h3><b>handlers.jsonhandler</b> Module</h3>

 

 JSON-related content handling.
<dl>
<dt><b>class gabbi.handlers.jsonhandler.JSONHandler</b>
<dd> Bases: <b>gabbi.handlers.base.ContentHandler</b> 

 A ContentHandler for JSON
<dt>&bull;
<dd> Structured test <b>data</b> is turned into JSON when request content-type is JSON.
<dt>&bull;
<dd> Response bodies that are JSON strings are made into Python data on the test <b>response_data</b> attribute when the response content-type is JSON.
<dt>&bull;
<dd> A <b>response_json_paths</b> response handler is added.
<dt>&bull;
<dd> JSONPaths in $RESPONSE substitutions are supported.
<dt><b>static accepts(content_type)</b>
<dd>
<dt><b>action(test, path, value=None)</b>
<dd> Test json_paths against json data.
<dt><b>static dumps(data, pretty=False)</b>
<dd>
<dt><b>static extract_json_path_value(data, path)</b>
<dd> Extract the value at JSON Path path from the data. 

 The input data is a Python datastructure, not a JSON string.
<dt><b>static loads(data)</b>
<dd>
<dt><b>classmethod replacer(response_data, match)</b>
<dd>
<dt><b>test_key_suffix = 'json_paths'</b>
<dd>
<dt><b>test_key_value = {}</b>
<dd></dl>

<h2>SUITE MODULE</h2>

 

 A TestSuite for containing gabbi tests. 

 This suite has two features: the contained tests are ordered and there are suite-level fixtures that operate as context managers.
<dl>
<dt><b>class gabbi.suite.GabbiSuite(tests=())</b>
<dd> Bases: <b>unittest.suite.TestSuite</b> 

 A TestSuite with fixtures. 

 The suite wraps the tests with a set of nested context managers that operate as fixtures. 

 If a fixture raises unittest.case.SkipTest during setup, all the tests in this suite will be skipped.
<dt><b>run(result, debug=False)</b>
<dd> Override TestSuite run to start suite-level fixtures. 

 To avoid exception confusion, use a null Fixture when there are no fixtures.
<dt><b>start(result)</b>
<dd> Start fixtures when using pytest.
<dt><b>stop()</b>
<dd> Stop fixtures when using pytest.
<dt><b>gabbi.suite.noop(*args)</b>
<dd> A noop method used to disable collected tests.</dl>

<h2>RUNNER MODULE</h2>

 

 Implementation of a command-line runner for gabbi files (AKA suites).
<dl>
<dt><b>gabbi.runner.extract_file_paths(argv)</b>
<dd> Extract command-line arguments following the <i>--</i> end-of-options delimiter, if any.
<dt><b>gabbi.runner.initialize_handlers(response_handlers)</b>
<dd>
<dt><b>gabbi.runner.load_response_handlers(import_path)</b>
<dd> Load and return custom response handlers from the given Python package or module. 

 The import path references either a specific response handler class (&quot;package.module:class&quot;) or a module that contains one or more response handler classes (&quot;package.module&quot;). 

 For the latter, the module is expected to contain a <b>gabbi_response_handlers</b> object, which is either a list of response handler classes or a function returning such a list.
<dt><b>gabbi.runner.run()</b>
<dd> Run simple tests from STDIN. 

 This command provides a way to run a set of tests encoded in YAML that is provided on STDIN. No fixtures are supported, so this is primarily designed for use with real running services. 

 Host and port information may be provided in three different ways:
<dt>&bull;
<dd> In the URL value of the tests.
<dt>&bull;
<dd> In a <i>host</i> or <i>host:port</i> argument on the command line.
<dt>&bull;
<dd> In a URL on the command line. 

 An example run might looks like this: 

 <pre>
gabbi-run example.com:9999 &lt; mytest.yaml
</pre> 

 or: 

 <pre>
gabbi-run <a rel="nofollow" HREF="http://example.com:999">http://example.com:999</a> &lt; mytest.yaml
</pre> 

 It is also possible to provide a URL prefix which can be useful if the target application might be mounted in different locations. An example: 

 <pre>
gabbi-run example.com:9999 /mountpoint &lt; mytest.yaml
</pre> 

 or: 

 <pre>
gabbi-run <a rel="nofollow" HREF="http://example.com:9999/mountpoint">http://example.com:9999/mountpoint</a> &lt; mytest.yaml
</pre> 

 Use <i>-x</i> or <i>--failfast</i> to abort after the first error or failure: 

 <pre>
gabbi-run -x example.com:9999 /mountpoint &lt; mytest.yaml
</pre> 

 Multiple files may be named as arguments, separated from other arguments by a <b>--</b>. Each file will be run as a separate test suite: 

 <pre>
gabbi-run <a rel="nofollow" HREF="http://example.com">http://example.com</a> -- /path/to/x.yaml /path/to/y.yaml
</pre> 

 Output is formatted as unittest summary information.
<dt><b>gabbi.runner.run_suite(handle, handler_objects, host, port, prefix, force_ssl=False, failfast=False)</b>
<dd> Run the tests from the YAML in handle.</dl>

<h2>REPORTER MODULE</h2>

 

 TestRunner and TestResult for gabbi-run.
<dl>
<dt><b>class gabbi.reporter.ConciseTestResult(stream, descriptions, verbosity)</b>
<dd> Bases: <b>unittest.runner.TextTestResult</b> 

 A TextTestResult with simple but useful output. 

 If the output is a tty or GABBI_FORCE_COLOR is set in the environment, output will be colorized.
<dt><b>addError(test, err)</b>
<dd>
<dt><b>addExpectedFailure(test, err)</b>
<dd>
<dt><b>addFailure(test, err)</b>
<dd>
<dt><b>addSkip(test, reason)</b>
<dd>
<dt><b>addSuccess(test)</b>
<dd>
<dt><b>addUnexpectedSuccess(test)</b>
<dd>
<dt><b>getDescription(test)</b>
<dd>
<dt><b>printErrorList(flavor, errors)</b>
<dd>
<dt><b>startTest(test)</b>
<dd>
<dt><b>class gabbi.reporter.ConciseTestRunner(stream=&lt;open file '&lt;stderr&gt;', mode 'w' at 0x7f4c0e5a81e0&gt;, descriptions=True, verbosity=1, failfast=False, buffer=False, resultclass=None)</b>
<dd> Bases: <b>unittest.runner.TextTestRunner</b> 

 A TextTestRunner that uses ConciseTestResult for reporting results.
<dt><b>resultclass</b>
<dd> alias of <b>ConciseTestResult</b>
<dt><b>class gabbi.reporter.PyTestResult(stream=None, descriptions=None, verbosity=None)</b>
<dd> Bases: <b>unittest.result.TestResult</b> 

 Wrap a test result to allow it to work with pytest. 

 The main behaviors here are:
<dt>&bull;
<dd> to turn what had been exceptions back into exceptions
<dt>&bull;
<dd> use pytest's skip and xfail methods
<dt><b>addError(test, err)</b>
<dd>
<dt><b>addExpectedFailure(test, err)</b>
<dd>
<dt><b>addFailure(test, err)</b>
<dd>
<dt><b>addSkip(test, reason)</b>
<dd></dl>

<h2>UTILS MODULE</h2>

 

 Utility functions grab bag.
<dl>
<dt><b>gabbi.utils.create_url(base_url, host, port=None, prefix='', ssl=False)</b>
<dd> Given pieces of a path-based url, return a fully qualified url.
<dt><b>gabbi.utils.decode_response_content(header_dict, content)</b>
<dd> Decode content to a proper string.
<dt><b>gabbi.utils.extract_content_type(header_dict, default='application/binary')</b>
<dd> Extract parsed content-type from headers.
<dt><b>gabbi.utils.get_colorizer(stream)</b>
<dd> Return a function to colorize a string. 

 Only if stream is a tty .
<dt><b>gabbi.utils.host_info_from_target(target, prefix=None)</b>
<dd> Turn url or host:port and target into test destination.
<dt><b>gabbi.utils.load_yaml(handle=None, yaml_file=None)</b>
<dd> Read and parse any YAML file or filehandle. 

 Let exceptions flow where they may. 

 If no file or handle is provided, read from STDIN.
<dt><b>gabbi.utils.not_binary(content_type)</b>
<dd> Decide if something is content we'd like to treat as a string.
<dt><b>gabbi.utils.parse_content_type(content_type, default_charset='utf-8')</b>
<dd> Parse content type value for media type and charset.</dl>

<h2>EXCEPTION MODULE</h2>

 

 Gabbi specific exceptions.
<dl>
<dt><b>exception gabbi.exception.GabbiFormatError</b>
<dd> Bases: <b>exceptions.ValueError</b> 

 An exception to encapsulate poorly formed test data.
<dt><b>exception gabbi.exception.GabbiSyntaxWarning</b>
<dd> Bases: <b>exceptions.SyntaxWarning</b> 

 A warning about syntax that is not desirable.</dl>

<h2>HTTPCLIENT MODULE</h2>

 

 Subclass of Http class for verbosity.
<dl>
<dt><b>class gabbi.httpclient.Http(num_pools=10, headers=None, **connection_pool_kw)</b>
<dd> Bases: <b>urllib3.poolmanager.PoolManager</b> 

 A subclass of the urllib3.PoolManager to munge the data. 

 This transforms the response to look more like what httplib2 provided when it was used as the httpclient.
<dt><b>request(absolute_uri, method, body, headers, redirect)</b>
<dd>
<dt><b>class gabbi.httpclient.VerboseHttp(**kwargs)</b>
<dd> Bases: <b>gabbi.httpclient.Http</b> 

 A subclass of Http that verbosely reports on activity. 

 If the output is a tty or <b>GABBI_FORCE_COLOR</b> is set in the environment, then output will be colorized according to <b>COLORMAP</b>. 

 Output can include request and response headers, request and response body content (if of a printable content-type), or both. 

 The color of the output has reasonable defaults. These may be overridden by setting the following environment variables
<dt>&bull;
<dd> GABBI_CAPTION_COLOR
<dt>&bull;
<dd> GABBI_HEADER_COLOR
<dt>&bull;
<dd> GABBI_REQUEST_COLOR
<dt>&bull;
<dd> GABBI_STATUS_COLOR 

 to any of: BLACK RED GREEN YELLOW BLUE MAGENTA CYAN WHITE
<dt><b>COLORMAP = {'status': 'CYAN', 'caption': 'BLUE', 'request': 'CYAN', 'header': 'YELLOW'}</b>
<dd>
<dt><b>HEADER_BLACKLIST = ['status', 'reason']</b>
<dd>
<dt><b>REQUEST_PREFIX = '&gt;'</b>
<dd>
<dt><b>RESPONSE_PREFIX = '&lt;'</b>
<dd>
<dt><b>request(absolute_uri, method, body, headers, redirect)</b>
<dd> Display request parameters before requesting.
<dt><b>gabbi.httpclient.get_http(verbose=False, caption='')</b>
<dd> Return an Http class for making requests.</dl>

<h2>JSON_PARSER MODULE</h2>

 

 Keep one single global jsonpath parser.
<dl>
<dt><b>gabbi.json_parser.parse(path)</b>
<dd> Parse a JSONPath expression use the global parser. 

 Gabbi is a tool for running HTTP tests where requests and responses are expressed as declarations in a collection of YAML files. The simplest test looks like this: 

 <pre>
tests:
- name: A test
  GET: /api/resources/id
</pre> 

 See the rest of these docs for more details on the many features and formats for setting request headers and bodies and evaluating responses. 

 The name is derived from &quot;gabby&quot;: excessively talkative. In a test environment having visibility of what a test is actually doing is a good thing. This is especially true when the goal of a test is to test the HTTP, not the testing infrastructure. Gabbi tries to put the HTTP interaction in the foreground of testing. 

 Tests can be run using <i>unittest</i> style test runners or py.test or from the command line with a <b>gabbi-run</b> script. 

 If you want to get straight to creating tests look at <b>example</b>, the test files in the <i>source distribution</i> and <b>format</b>. A <i>gabbi-demo</i> repository provides a tutorial of using gabbi to build an API, via the commit history of the repo.</dl>

<h2>PURPOSE</h2>

 

 Gabbi works to bridge the gap between human readable YAML files (see <b>format</b> for details) that represent HTTP requests and expected responses and the rather complex world of automated testing. 

 Each YAML file represents an ordered list of HTTP requests along with the expected responses. This allows a single file to represent a process in the API being tested. For example:
<dl>
<dt>&bull;
<dd> Create a resource.
<dt>&bull;
<dd> Retrieve a resource.
<dt>&bull;
<dd> Delete a resource.
<dt>&bull;
<dd> Retrieve a resource again to confirm it is gone. 

 At the same time it is still possible to ask gabbi to run just one request. If it is in a sequence of tests, those tests prior to it in the YAML file will be run (in order). In any single process any test will only be run once. Concurrency is handled such that one file runs in one process. 

 These features mean that it is possible to create tests that are useful for both humans (as tools for learning, improving and developing APIs) and automated CI systems. 

 Significant flexibility and power is available in the <b>format</b> to make it relatively straightforward to test existing complex APIs. This extended functionality includes the use of <i>JSONPath</i> to query response bodies and templating of test data to allow access to the prior HTTP response in the current request. For APIs which do not use JSON additional <b>handlers</b> can be created. 

 Care should be taken when using this functionality when you are creating a new API. If your API is so complex that it needs complex test files then you may wish to take that as a sign that your API itself too complex. One goal of gabbi is to encourage transparent and comprehensible APIs. 

 Though gabbi is written in Python and under the covers uses <b>unittest</b> data structures and processes, there is no requirement that the <b>host</b> be a Python-based service. Anything talking HTTP can be tested. A <b>runner</b> makes it possible to simply create YAML files and point them at a running server.</dl>

<h2>AUTHOR</h2>

 Chris Dent 

<h2>Index</h2>



<dt><a HREF="#lbAG">FIXTURES</a>
<dd>
<dt><a HREF="#lbAH">RESPONSE HANDLERS</a>
<dd>
<dt><a HREF="#lbAI">SUBSTITUTION</a>
<dd>
<dt><a HREF="#lbAJ">DATA</a>
<dd>
<dt><a HREF="#lbAK">UNITTEST STYLE LOADER</a>
<dd>
<dt><a HREF="#lbAL">PYTEST</a>
<dd>
<dt><a HREF="#lbAM">EXTENSIONS</a>
<dd>


<dt><a HREF="#lbAO">1.27.0</a>
<dd>
<dt><a HREF="#lbAP">1.26.0</a>
<dd>
<dt><a HREF="#lbAQ">1.25.0</a>
<dd>
<dt><a HREF="#lbAR">1.24.0</a>
<dd>
<dt><a HREF="#lbAS">1.23.0</a>
<dd>
<dt><a HREF="#lbAT">1.22.0</a>
<dd>
<dt><a HREF="#lbAU">1.21.0</a>
<dd>
<dt><a HREF="#lbAV">1.20.0</a>
<dd>
<dt><a HREF="#lbAW">1.19.1</a>
<dd>
<dt><a HREF="#lbAX">1.19.0</a>
<dd>
<dt><a HREF="#lbAY">1.17.0</a>
<dd>
<dt><a HREF="#lbAZ">1.16.0</a>
<dd>
<dt><a HREF="#lbBA">1.13.0</a>
<dd>
<dt><a HREF="#lbBB">1.11.0</a>
<dd>
<dt><a HREF="#lbBC">1.7.0</a>
<dd>
<dt><a HREF="#lbBD">1.4.0 AND 1.5.0</a>
<dd>
<dt><a HREF="#lbBE">1.3.0</a>
<dd>
<dt><a HREF="#lbBF">1.2.0</a>
<dd>
<dt><a HREF="#lbBG">1.1.0</a>
<dd>
<dt><a HREF="#lbBH">1.0.0</a>
<dd>
<dt><a HREF="#lbBI">GENERAL</a>
<dd>


<dt><a HREF="#lbBK">WORKAROUNDS</a>
<dd>


<dt><a HREF="#lbBM">TESTING STYLE</a>
<dd>


<dt><a HREF="#lbBP">CASE MODULE</a>
<dd>
<dt><a HREF="#lbBQ">DRIVER MODULE</a>
<dd>
<dt><a HREF="#lbBR">SUITEMAKER MODULE</a>
<dd>
<dt><a HREF="#lbBS">FIXTURE MODULE</a>
<dd>
<dt><a HREF="#lbBT">HANDLERS MODULE</a>
<dd>


<dt><a HREF="#lbBX">SUITE MODULE</a>
<dd>
<dt><a HREF="#lbBY">RUNNER MODULE</a>
<dd>
<dt><a HREF="#lbBZ">REPORTER MODULE</a>
<dd>
<dt><a HREF="#lbCA">UTILS MODULE</a>
<dd>
<dt><a HREF="#lbCB">EXCEPTION MODULE</a>
<dd>
<dt><a HREF="#lbCC">HTTPCLIENT MODULE</a>
<dd>
<dt><a HREF="#lbCD">JSON_PARSER MODULE</a>
<dd>
<dt><a HREF="#lbCE">PURPOSE</a>
<dd>
<dt><a HREF="#lbCF">AUTHOR</a>
<dd></dl>
