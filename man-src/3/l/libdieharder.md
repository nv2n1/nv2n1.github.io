---
title: "libdieharder(3)"
name: "libdieharder"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libdieharder/"
description: "libdieharder – A testing and benchmarking library for random number generators"
---

<h2>NAME</h2>
<p> libdieharder &#8211; A testing and benchmarking library for random number generators </p>
<h2>SYNOPSIS</h2>
<p> <code>#include dieharder.h</code> </p>
<p> <code>void run_user_template()</code><br />
 <code>{</code> </p>
<p> <code>Test **user_template_test;</code><br />
 <code>/*</code><br />
 <code> * Create the test</code><br />
 <code> */</code><br />
 <code>user_template_test = create_test(&amp;user_template_dtest,tsamples,psamples,&amp;user_template);</code> </p>
<p> <code>/*</code><br />
 <code> * Set any GLOBAL data used by the test.</code><br />
 <code> */</code><br />
 <code>user_template_lag = (int)x_user;</code> </p>
<p> <code>/*</code><br />
 <code> * Show the standard test header</code><br />
 <code> */</code><br />
 <code>show_test_header(&amp;user_template_dtest,user_template_test);</code> </p>
<p> <code>/*</code><br />
 <code> * Call the test</code><br />
 <code> */</code><br />
 <code>std_test(&amp;user_template_dtest,user_template_test);</code> </p>
<p> <code>/*</code><br />
 <code> * This almost certainly belongs in the show_test_results section,</code><br />
 <code> * possibly with additional conditionals rejecting test results involving</code><br />
 <code> * rewinds, period.</code><br />
 <code> */</code><br />
 <code>if(strncmp(<br />
 </code> <code> printf(# %u rands were used in this test,file_input_get_rtot(rng));</code><br />
 <code> printf(# The file %s was rewound %u times,gsl_rng_name(rng),file_input_get_rewind_cnt(rng));</code><br />
 <code>}</code> </p>
<p> <code>/*</code><br />
 <code> * Show standard test results</code><br />
 <code> */.</code><br />
 <code>show_test_results(&amp;user_template_dtest,user_template_test);</code> </p>
<p> <code>}</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>libdieharder</code> </p>
<p> The libdieharder library provides an API to user interface programs wishing to call dieharder tests. Commands are defined for creating tests, initializing the tests and running the tests. Showing the results is of course the responsibility of the UI. </p>
<p> libdieharder also wraps certain additional random number generators so that they can be tested. libdieharder can be default test all the random number generators in the Gnu Scientific Library plus these additional generators (which include &quot;generators&quot; for reading in numbers from a file). </p>
<p> libdieharder is extensible. It is fairly easy to add additional test &quot;objects&quot; or random number generators using existing sources as templates. </p>
<p> The API will be documented in more detail as the project approaches completion. In the meantime, it is strongly recommended that users wishing to call the library use the source of the dieharder tty UI as a template and list of all currently supported objects, as this is the primary libdieharder debugging vehicle in addition to being the current &quot;standard&quot; application of the library. </p>
<h2>PUBLICATION RULES</h2>
<p> <code>libdieharder</code> is entirely original code and can be modified and used at will by any user, provided that: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>a)&nbsp;<wbr>The original copyright notices are maintained and that the source, including all modifications, is made publically available at the time of any derived publication. This is open source software according to the precepts and spirit of the Gnu Public License. See the accompanying file COPYING, which also must accompany any redistribution. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>b)&nbsp;<wbr>The author of the code&nbsp;<wbr>(Robert G. Brown)&nbsp;<wbr>is appropriately acknowledged and referenced in any derived publication. It is strongly suggested that George Marsaglia and the Diehard suite and the various authors of the Statistical Test Suite be similarly acknowledged, although this suite shares no actual code with these random number test suites. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>c)&nbsp;<wbr>Full responsibility for the accuracy, suitability, and effectiveness of the program rests with the users and/or modifiers. As is clearly stated in the accompanying copyright.h: </p>
<p> THE COPYRIGHT HOLDERS DISCLAIM ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE. </p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> The author of this suite gratefully acknowledges George Marsaglia (the author of the diehard test suite) and the various authors of NIST Special Publication 800-22 (which describes the Statistical Test Suite for testing pseudorandom number generators for cryptographic applications), for excellent descriptions of the tests therein. These descriptions enabled this suite to be developed with a clean copyright, licensable under the GPL. </p>
<p> The author also wishes to reiterate that the academic correctness and accuracy of the implementation of these tests is his sole responsibility and not that of the authors of the Diehard or STS suites. This is especially true where he has seen fit to modify those tests from their strict original descriptions. </p>
<h2>COPYRIGHT</h2>
<p> GPL 2b; see the file COPYING that accompanies the source of this program. This is the &quot;standard Gnu General Public License version 2 or any later version&quot;, with the one minor (humorous) &quot;Beverage&quot; modification listed below. Note that this modification is probably not legally defensible and can be followed really pretty much according to the honor rule. </p>
<p> As to my personal preferences in beverages, red wine is great, beer is delightful, and Coca Cola or coffee or tea or even milk acceptable to those who for religious or personal reasons wish to avoid stressing my liver. </p>
<p> <code>The Beverage Modification to the GPL:</code> </p>
<p> Any satisfied user of this software shall, upon meeting the primary author(s) of this software for the first time under the appropriate circumstances, offer to buy him or her or them a beverage. This beverage may or may not be alcoholic, depending on the personal ethical and moral views of the offerer. The beverage cost need not exceed one U.S. dollar (although it certainly may at the whim of the offerer:-) and may be accepted or declined with no further obligation on the part of the offerer. It is not necessary to repeat the offer after the first meeting, but it can&#8217;t hurt&#8230; </p>
<h2>Index</h2>
