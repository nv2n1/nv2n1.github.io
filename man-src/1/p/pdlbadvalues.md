---
title: "pdlbadvalues(1)"
name: "pdlbadvalues"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdlbadvalues/"
description: "PDL::BadValues – Discussion of bad value support in PDL"
---

<p>PDL::BadValues &#8211; Discussion of bad value support in PDL </p>
<h2>Description</h2>
<h3>What are bad values and why should I bother with them?</h3>
<p>Sometimes it&#8217;s useful to be able to specify a certain value is &#8216;bad&#8217; or &#8216;missing&#8217;; for example CCDs used in astronomy produce 2D images which are not perfect since certain areas contain invalid data due to imperfections in the detector. Whilst <font SIZE="-1">PDL</font>&#8216;s powerful index routines and all the complicated business with dataflow, slices, etc etc mean that these regions can be ignored in processing, it&#8217;s awkward to do. It would be much easier to be able to say <tt>&quot;$c = $a + $b&quot;</tt> and leave all the hassle to the computer. </p>
<p> If you&#8217;re not interested in this, then you may (rightly) be concerned with how this affects the speed of <font SIZE="-1">PDL,</font> since the overhead of checking for a bad value at each operation can be large. Because of this, the code has been written to be as fast as possible &#8211; particularly when operating on piddles which do not contain bad values. In fact, you should notice essentially no speed difference when working with piddles which do not contain bad values. </p>
<p> However, if you do not want bad values, then <font SIZE="-1">PDL</font>&#8216;s <tt>&quot;WITH_BADVAL&quot;</tt> configuration option comes to the rescue; if set to 0 or undef, the bad-value support is ignored. About the only time I think you&#8217;ll need to use this &#8211; I admit, I&#8217;m biased ;) &#8211; is if you have limited disk or memory space, since the size of the code is increased (see below). </p>
<p> You may also ask &#8216;well, my computer supports <font SIZE="-1">IEEE</font> NaN, so I already have this&#8217;. Well, yes and no &#8211; many routines, such as <tt>&quot;y=sin(x)&quot;</tt>, will propagate NaN&#8217;s without the user having to code differently, but routines such as <tt>&quot;qsort&quot;</tt>, or finding the median of an array, need to be re-coded to handle bad values. For floating-point datatypes, <tt>&quot;NaN&quot;</tt> and <tt>&quot;Inf&quot;</tt> are used to flag bad values <i></i><font SIZE="-1"><i>IF</i></font><i></i> the option <tt>&quot;BADVAL_USENAN&quot;</tt> is set to 1 in your config file. Otherwise special values are used (Default bad values). I do not have any benchmarks to see which option is faster. </p>
<p> There is an experimental feature <tt>&quot;BADVAL_PER_PDL&quot;</tt> which, if set, allows you to have different bad values for separate piddles of the same type. This currently does not work with the <tt>&quot;BADVAL_USENAN&quot;</tt> option; if both are set then <font SIZE="-1">PDL</font> will ignore the <tt>&quot;BADVAL_USENAN&quot;</tt> value.</p>
<h3>Code increase due to bad values</h3>
<p>The following comparison is out of date! </p>
<p> On an i386 machine running Linux and Perl 5.005_03, I measured the following sizes (the Slatec code was compiled in, but none of the other options: e.g., <font SIZE="-1">FFTW, GSL,</font> and TriD were):</p>
<dl>
<dt><font SIZE="-1">WITH_BADVAL</font> = 0</p>
<dd>Size of blib directory after a successful make = <code>4963 kb</code>: blib/arch = 2485 kb and blib/lib = 1587 kb.</p>
<dt><font SIZE="-1">WITH_BADVAL</font> = 1</p>
<dd>Size of blib directory after a successful make = <code>5723 kb</code>: blib/arch = 3178 kb and blib/lib = 1613 kb.</dl>
<p> So, the overall increase is <i>only</i> 15% &#8211; not much to pay for all the wonders that bad values provides ;) </p>
<p> The source code used for this test had the vast majority of the core routines (eg those in Basic/) converted to use bad values, whilst very few of the &#8216;external&#8217; routines (i.e. everything else in the <font SIZE="-1">PDL</font> distribution) had been changed.</p>
<h3>A quick overview</h3>
<pre> pdl&gt; p $PDL::Bad::Status
 1
 pdl&gt; $a = sequence(4,3);
 pdl&gt; p $a
 [
 [ 0 1 2 3]
 [ 4 5 6 7]
 [ 8 9 10 11]
 ]
 pdl&gt; $a = $a-&gt;setbadif( $a % 3 == 2 )
 pdl&gt; p $a
 [
 [ 0 1 BAD 3]
 [ 4 BAD 6 7]
 [BAD 9 10 BAD]
 ]
 pdl&gt; $a *= 3
 pdl&gt; p $a
 [
 [ 0 3 BAD 9]
 [ 12 BAD 18 21]
 [BAD 27 30 BAD]
 ]
 pdl&gt; p $a-&gt;sum
 120</pre>
<p><tt>&quot;demo bad&quot;</tt> and <tt>&quot;demo bad2&quot;</tt> within perldl or pdl2 gives a demonstration of some of the things possible with bad values. These are also available on <font SIZE="-1">PDL</font>&#8216;s web-site, at <i><a rel="nofollow" href="http://pdl.perl.org/demos/">http://pdl.perl.org/demos/</a></i>. See PDL::Bad for useful routines for working with bad values and <i>t/bad.t</i> to see them in action. </p>
<p> The intention is to:</p>
<dl>
<dt>&bull;</p>
<dd>not significantly affect <font SIZE="-1">PDL</font> for users who don&#8217;t need bad value support</p>
<dt>&bull;</p>
<dd>be as fast as possible when bad value support is installed</dl>
<p> If you never want bad value support, then you set <tt>&quot;WITH_BADVAL&quot;</tt> to 0 in <i>perldl.conf</i>; <font SIZE="-1">PDL</font> then has no bad value support compiled in, so will be as fast as it used to be. </p>
<p> However, in most cases, the bad value support has a negligible affect on speed, so you should set <tt>&quot;WITH_CONFIG&quot;</tt> to 1! One exception is if you are low on memory, since the amount of code produced is larger (but only by about 15% &#8211; see &#8220;Code increase due to bad values&#8221;). </p>
<p> To find out if <font SIZE="-1">PDL</font> has been compiled with bad value support, look at the values of either <tt>$PDL::Config{WITH_BADVAL}</tt> or <tt>$PDL::Bad::Status</tt> &#8211; if true then it has been. </p>
<p> To find out if a routine supports bad values, use the <tt>&quot;badinfo&quot;</tt> command in perldl or pdl2 or the <tt>&quot;-b&quot;</tt> option to pdldoc. This facility is currently a &#8216;proof of concept&#8217; (or, more realistically, a quick hack) so expect it to be rough around the edges. </p>
<p> Each piddle contains a flag &#8211; accessible via <tt>&quot;$pdl-&gt;badflag&quot;</tt> &#8211; to say whether there&#8217;s any bad data present:</p>
<dl>
<dt>&bull;</p>
<dd>If <code>false/0</code>, which means there&#8217;s no bad data here, the code supplied by the <tt>&quot;Code&quot;</tt> option to <tt>&quot;pp_def()&quot;</tt> is executed. This means that the speed should be very close to that obtained with <tt>&quot;WITH_BADVAL=0&quot;</tt>, since the only overhead is several accesses to a bit in the piddles state variable.</p>
<dt>&bull;</p>
<dd>If <code>true/1</code>, then this says there <i></i><font SIZE="-1"><i>MAY</i></font><i></i> be bad data in the piddle, so use the code in the <tt>&quot;BadCode&quot;</tt> option (assuming that the <tt>&quot;pp_def()&quot;</tt> for this routine has been updated to have a BadCode key). You get all the advantages of threading, as with the <tt>&quot;Code&quot;</tt> option, but it will run slower since you are going to have to handle the presence of bad values.</dl>
<p> If you create a piddle, it will have its bad-value flag set to 0. To change this, use <tt>&quot;$pdl-&gt;badflag($new_bad_status)&quot;</tt>, where <tt>$new_bad_status</tt> can be 0 or 1. When a routine creates a piddle, its bad-value flag will depend on the input piddles: unless over-ridden (see the <tt>&quot;CopyBadStatusCode&quot;</tt> option to <tt>&quot;pp_def&quot;</tt>), the bad-value flag will be set true if any of the input piddles contain bad values. To check that a piddle really contains bad data, use the <tt>&quot;check_badflag&quot;</tt> method. </p>
<p> <i></i><font SIZE="-1"><i>NOTE</i></font><i></i>: propogation of the badflag </p>
<p> If you change the badflag of a piddle, this change is propagated to all the <i>children</i> of a piddle, so </p>
<pre> pdl&gt; $a = zeroes(20,30);
 pdl&gt; $b = $a-&gt;slice('0:10,0:10');
 pdl&gt; $c = $b-&gt;slice(',(2)');
 pdl&gt; print &quot;&gt;&gt;c: &quot;, $c-&gt;badflag, &quot;
&quot;;
 &gt;&gt;c: 0
 pdl&gt; $a-&gt;<a href="//www.systutorials.com/docs/linux/man/1-badflag/">badflag</a>(1);
 pdl&gt; print &quot;&gt;&gt;c: &quot;, $c-&gt;badflag, &quot;
&quot;;
 &gt;&gt;c: 1</pre>
<p><i>No</i> change is made to the parents of a piddle, so </p>
<pre> pdl&gt; print &quot;&gt;&gt;a: &quot;, $a-&gt;badflag, &quot;
&quot;;
 &gt;&gt;a: 1
 pdl&gt; $c-&gt;badflag(0);
 pdl&gt; print &quot;&gt;&gt;a: &quot;, $a-&gt;badflag, &quot;
&quot;;
 &gt;&gt;a: 1</pre>
<p>Thoughts:</p>
<dl>
<dt>&bull;</p>
<dd>the badflag can <font SIZE="-1">ONLY</font> be cleared <font SIZE="-1">IF</font> a piddle has <font SIZE="-1">NO</font> parents, and that this change will propagate to all the children of that piddle. I am not so keen on this anymore (too awkward to code, for one).</p>
<dt>&bull;</p>
<dd><tt>&quot;$a-&gt;<a href="/docs/linux/man/1-badflag/">badflag</a>(1)&quot;</tt> should propagate the badflag to <font SIZE="-1">BOTH</font> parents and children.</dl>
<p> This shouldn&#8217;t be hard to implement (although an initial attempt failed!). Does it make sense though? There&#8217;s also the issue of what happens if you change the badvalue of a piddle &#8211; should these propagate to children/parents (yes) or whether you should only be able to change the badvalue at the &#8216;top&#8217; level &#8211; i.e. those piddles which do not have parents. </p>
<p> The <tt>&quot;orig_badvalue()&quot;</tt> method returns the compile-time value for a given datatype. It works on piddles, PDL::Type objects, and numbers &#8211; eg </p>
<pre> $pdl-&gt;orig_badvalue(), byte-&gt;orig_badvalue(), and <a href="//www.systutorials.com/docs/linux/man/4-orig_badvalue/">orig_badvalue</a>(4).</pre>
<p>It also has a horrible name&#8230; </p>
<p> To get the current bad value, use the <tt>&quot;badvalue()&quot;</tt> method &#8211; it has the same syntax as <tt>&quot;orig_badvalue()&quot;</tt>. </p>
<p> To change the current bad value, supply the new number to badvalue &#8211; eg </p>
<pre> $pdl-&gt;badvalue(2.3), byte-&gt;<a href="//www.systutorials.com/docs/linux/man/2-badvalue/">badvalue</a>(2), badvalue(5,-3e34).</pre>
<p><i>Note</i>: the value is silently converted to the correct C type, and returned &#8211; i.e. <tt>&quot;byte-&gt;badvalue(-26)&quot;</tt> returns 230 on my Linux machine. It is also a <tt>&quot;nop&quot;</tt> for floating-point types when <tt>&quot;BADVAL_USENAN&quot;</tt> is true. </p>
<p> Note that changes to the bad value are <i></i><font SIZE="-1"><i>NOT</i></font><i></i> propagated to previously-created piddles &#8211; they will still have the bad value set, but suddenly the elements that were bad will become &#8216;good&#8217;, but containing the old bad value. See discussion below. It&#8217;s not a problem for floating-point types which use NaN, since you can not change their badvalue.</p>
<h3>Bad values and boolean operators</h3>
<p>For those boolean operators in PDL::Ops, evaluation on a bad value returns the bad value. Whilst this means that </p>
<pre> $mask = $img &gt; $thresh;</pre>
<p>correctly propagates bad values, it <i>will</i> cause problems for checks such as </p>
<pre> do_something() if any( $img &gt; $thresh );</pre>
<p>which need to be re-written as something like </p>
<pre> do_something() if any( setbadtoval( ($img &gt; $thresh), 0 ) );</pre>
<p>When using one of the &#8216;projection&#8217; functions in PDL::Ufunc &#8211; such as orover &#8211; bad values are skipped over (see the documentation of these functions for the current (poor) handling of the case when all elements are bad).</p>
<h3>A bad value for each piddle, and related issues</h3>
<p>An <code>experimental</code> option <tt>&quot;BADVAL_PER_PDL&quot;</tt> has been added to <i>perldl.conf</i> to allow per-piddle bad values. The documentation has not been updated to account for this change. </p>
<p> The following is relevant only for integer types, and for floating-point types if <tt>&quot;BADVAL_USENAN&quot;</tt> was not set when <font SIZE="-1">PDL</font> was built. </p>
<p> Currently, there is one bad value for each datatype. The code is written so that we could have a separate bad value for each piddle (stored in the pdl structure) &#8211; this would then remove the current problem of: </p>
<pre> pdl&gt; $a = byte( 1, 2, byte-&gt;badvalue, 4, 5 );
 pdl&gt; p $a;
 [1 2 255 4 5]
 pdl&gt; $a-&gt;<a href="//www.systutorials.com/docs/linux/man/1-badflag/">badflag</a>(1)
 pdl&gt; p $a;
 [1 2 BAD 4 5]
 pdl&gt; byte-&gt;badvalue(0);
 pdl&gt; p $a;
 [1 2 255 4 5]</pre>
<p>ie the bad value in <tt>$a</tt> has lost its <i>bad</i> status using the current implementation. It would almost certainly cause problems elsewhere though!</p>
<h2>Implementation Details</h2>
<p>During a <tt>&quot;perl Makefile.PL&quot;</tt>, the file <i>Basic/Core/badsupport.p</i> is created; this file contains the values of the <tt>&quot;WITH_BADVAL&quot;</tt>, <tt>&quot;BADVAL_USENAN&quot;</tt> and <tt>&quot;BADVAL_PER_PDL&quot;</tt> variables, and should be used by code that is executed before the <i>PDL::Config</i> file is created (e.g. <i>Basic/Core/pdlcore.c.PL</i>. However, most <font SIZE="-1">PDL</font> code will just need to access the <tt>%PDL::Config</tt> array (e.g. <i>Basic/Bad/bad.pd</i>) to find out whether bad-value support is required. </p>
<p> A new flag has been added to the state of a piddle &#8211; <tt>&quot;PDL_BADVAL&quot;</tt>. If unset, then the piddle does not contain bad values, and so all the support code can be ignored. If set, it does not guarantee that bad values are present, just that they should be checked for. Thanks to Christian, <tt>&quot;badflag()&quot;</tt> &#8211; which sets/clears this flag (see <i>Basic/Bad/bad.pd</i>) &#8211; will update <i></i><font SIZE="-1"><i>ALL</i></font><i></i> the children/grandchildren/etc of a piddle if its state changes (see <tt>&quot;badflag&quot;</tt> in <i>Basic/Bad/bad.pd</i> and <tt>&quot;propagate_badflag&quot;</tt> in <i>Basic/Core/Core.xs.PL</i>). It&#8217;s not clear what to do with parents: I can see the reason for propagating a &#8216;set badflag&#8217; request to parents, but I think a child should <font SIZE="-1">NOT</font> be able to clear the badflag of a parent. There&#8217;s also the issue of what happens when you change the bad value for a piddle. </p>
<p> The <tt>&quot;pdl_trans&quot;</tt> structure has been extended to include an integer value, <tt>&quot;bvalflag&quot;</tt>, which acts as a switch to tell the code whether to handle bad values or not. This value is set if any of the input piddles have their <tt>&quot;PDL_BADVAL&quot;</tt> flag set (although this code can be replaced by setting <tt>&quot;FindBadStateCode&quot;</tt> in pp_def). The logic of the check is going to get a tad more complicated if I allow routines to fall back to using the <tt>&quot;Code&quot;</tt> section for floating-point types (i.e. those routines with <tt>&quot;NoBadifNaN =&gt; 1&quot;</tt> when <tt>&quot;BADVAL_USENAN&quot;</tt> is true). </p>
<p> The bad values for the integer types are now stored in a structure within the Core <font SIZE="-1">PDL</font> structure &#8211; <tt>&quot;PDL.bvals&quot;</tt> (eg <i>Basic/Core/pdlcore.h.PL</i>); see also <tt>&quot;typedef badvals&quot;</tt> in <i>Basic/Core/pdl.h.PL</i> and the <font SIZE="-1">BOOT</font> code of <i>Basic/Core/Core.xs.PL</i> where the values are initialised to (hopefully) sensible values. See <i>PDL/Bad/bad.pd</i> for read/write routines to the values. </p>
<p> The addition of the <tt>&quot;BADVAL_PER_PDL&quot;</tt> option has resulted in additional changes to the internals of piddles. These changes are not documented yet.</p>
<h3>Why not make a <font SIZE="-1">PDL</font> subclass?</h3>
<p>The support for bad values could have been done as a <font SIZE="-1">PDL</font> sub-class. The advantage of this approach would be that you only load in the code to handle bad values if you actually want to use them. The downside is that the code then gets separated: any bug fixes/improvements have to be done to the code in two different files. With the present approach the code is in the same <tt>&quot;pp_def&quot;</tt> function (although there is still the problem that both <tt>&quot;Code&quot;</tt> and <tt>&quot;BadCode&quot;</tt> sections need updating).</p>
<h3>Default bad values</h3>
<p>The default/original bad values are set to (taken from the Starlink distribution): </p>
<pre> #include &lt;limits.h&gt;
 PDL_Byte == UCHAR_MAX
 PDL_Short == SHRT_MIN
 PDL_Ushort == USHRT_MAX
 PDL_Long == INT_MIN</pre>
<p>If <tt>&quot;BADVAL_USENAN == 0&quot;</tt>, then we also have </p>
<pre> PDL_Float == -FLT_MAX
 PDL_Double == -DBL_MAX</pre>
<p>otherwise all of <tt>&quot;NaN&quot;</tt>, <tt>&quot;+Inf&quot;</tt>, and <tt>&quot;-Inf&quot;</tt> are taken to be bad for floating-point types. In this case, the bad value can&#8217;t be changed, unlike the integer types.</p>
<h3>How do I change a routine to handle bad values?</h3>
<p>Examples can be found in most of the <i>*.pd</i> files in <i>Basic/</i> (and hopefully many more places soon!). Some of the logic might appear a bit unclear &#8211; that&#8217;s probably because it is! Comments appreciated. </p>
<p> All routines should automatically propagate the bad status flag to output piddles, unless you declare otherwise. </p>
<p> If a routine explicitly deals with bad values, you must provide this option to pp_def: </p>
<pre> HandleBad =&gt; 1</pre>
<p>This ensures that the correct variables are initialised for the <tt>$ISBAD</tt> etc macros. It is also used by the automatic document-creation routines to provide default information on the bad value support of a routine without the user having to type it themselves (this is in its early stages). </p>
<p> To flag a routine as <font SIZE="-1">NOT</font> handling bad values, use </p>
<pre> HandleBad =&gt; 0</pre>
<p>This <i>should</i> cause the routine to print a warning if it&#8217;s sent any piddles with the bad flag set. Primitive&#8217;s <tt>&quot;intover&quot;</tt> has had this set &#8211; since it would be awkward to convert &#8211; but I&#8217;ve not tried it out to see if it works. </p>
<p> If you want to handle bad values but not set the state of all the output piddles, or if it&#8217;s only one input piddle that&#8217;s important, then look at the <font SIZE="-1">PP</font> rules <tt>&quot;NewXSFindBadStatus&quot;</tt> and <tt>&quot;NewXSCopyBadStatus&quot;</tt> and the corresponding <tt>&quot;pp_def&quot;</tt> options:</p>
<dl>
<dt>FindBadStatusCode</p>
<dd>By default, <tt>&quot;FindBadStatusCode&quot;</tt> creates code which sets <tt>&quot;$PRIV(bvalflag)&quot;</tt> depending on the state of the bad flag of the input piddles: see <tt>&quot;findbadstatus&quot;</tt> in <i>Basic/Gen/PP.pm</i>. User-defined code should also store the value of <tt>&quot;bvalflag&quot;</tt> in the <tt>&quot;$BADFLAGCACHE()&quot;</tt> variable.</p>
<dt>CopyBadStatusCode</p>
<dd>The default code here is a bit simpler than for <tt>&quot;FindBadStatusCode&quot;</tt>: the bad flag of the output piddles are set if <tt>&quot;$BADFLAGCACHE()&quot;</tt> is true after the code has been evaluated. Sometimes <tt>&quot;CopyBadStatusCode&quot;</tt> is set to an empty string, with the responsibility of setting the badflag of the output piddle left to the <tt>&quot;BadCode&quot;</tt> section (e.g. the <tt>&quot;xxxover&quot;</tt> routines in <i>Basic/Primitive/primitive.pd</i>). </p>
<p> Prior to <font SIZE="-1">PDL 2.4.3</font> we used <tt>&quot;$PRIV(bvalflag)&quot;</tt> instead of <tt>&quot;$BADFLAGCACHE()&quot;</tt>. This is dangerous since the <tt>&quot;$PRIV()&quot;</tt> structure is not guaranteed to be valid at this point in the code.</dl>
<p> If you have a routine that you want to be able to use as in-place, look at the routines in <i>bad.pd</i> (or <i>ops.pd</i>) which use the <tt>&quot;in-place&quot;</tt> option to see how the bad flag is propagated to children using the <tt>&quot;xxxBadStatusCode&quot;</tt> options. I decided not to automate this as rules would be a little complex, since not every in-place op will need to propagate the badflag (eg unary functions). </p>
<p> If the option </p>
<pre> HandleBad =&gt; 1</pre>
<p>is given, then many things happen. For integer types, the readdata code automatically creates a variable called <tt>&quot;&lt;pdl name&gt;_badval&quot;</tt>, which contains the bad value for that piddle (see <tt>&quot;get_xsdatapdecl()&quot;</tt> in <i>Basic/Gen/PP/PdlParObjs.pm</i>). However, do not hard code this name into your code! Instead use macros (thanks to Tuomas for the suggestion): </p>
<pre> '$ISBAD(a(n=&gt;1))' expands to '$a(n=&gt;1) == a_badval'
 '$ISGOOD(a())' '$a() != a_badval'
 '$SETBAD(bob())' '$bob() = bob_badval'</pre>
<p>well, the <tt>&quot;$a(...)&quot;</tt> is expanded as well. Also, you can use a <tt>&quot;$&quot;</tt> before the pdl name, if you so wish, but it begins to look like line noise &#8211; eg <tt>&quot;$ISGOOD($a())&quot;</tt>. </p>
<p> If you cache a piddle value in a variable &#8212; eg <tt>&quot;index&quot;</tt> in <i>slices.pd</i> &#8212; the following routines are useful: </p>
<pre> '$ISBADVAR(c_var,pdl)' 'c_var == pdl_badval'
 '$ISGOODVAR(c_var,pdl)' 'c_var != pdl_badval'
 '$SETBADVAR(c_var,pdl)' 'c_var = pdl_badval'</pre>
<p>The following have been introduced, They may need playing around with to improve their use. </p>
<pre> '$PPISBAD(CHILD,[i]) 'CHILD_physdatap[i] == CHILD_badval'
 '$PPISGOOD(CHILD,[i]) 'CHILD_physdatap[i] != CHILD_badval'
 '$PPSETBAD(CHILD,[i]) 'CHILD_physdatap[i] = CHILD_badval'</pre>
<p>If <tt>&quot;BADVAL_USENAN&quot;</tt> is set, then it&#8217;s a bit different for <tt>&quot;float&quot;</tt> and <tt>&quot;double&quot;</tt>, where we consider <tt>&quot;NaN&quot;</tt>, <tt>&quot;+Inf&quot;</tt>, and <tt>&quot;-Inf&quot;</tt> all to be bad. In this case: </p>
<pre> ISBAD becomes finite(piddle) == 0
 ISGOOD finite(piddle) != 0
 SETBAD piddle = NaN</pre>
<p>where the value for NaN is discussed below in Handling NaN values. </p>
<p> This all means that you can change </p>
<pre> Code =&gt; '$a() = $b() + $c();'</pre>
<p>to </p>
<pre> BadCode =&gt; 'if ( $ISBAD(b()) || $ISBAD(c()) ) { 
 $SETBAD(a()); 
 } else {
 $a() = $b() + $c();
 }'</pre>
<p>leaving Code as it is. PP::PDLCode will then create a loop something like </p>
<pre> if ( __trans-&gt;bvalflag ) {
 threadloop over BadCode
 } else { 
 threadloop over Code
 }</pre>
<p>(it&#8217;s probably easier to just look at the <i>.xs</i> file to see what goes on).</p>
<h3>Going beyond the Code section</h3>
<p>Similar to <tt>&quot;BadCode&quot;</tt>, there&#8217;s <tt>&quot;BadBackCode&quot;</tt>, and <tt>&quot;BadRedoDimsCode&quot;</tt>. </p>
<p> Handling <tt>&quot;EquivCPOffsCode&quot;</tt> is a bit different: under the assumption that the only access to data is via the <tt>&quot;$EQUIVCPOFFS(i,j)&quot;</tt> macro, then we can automatically create the &#8216;bad&#8217; version of it; see the <tt>&quot;[EquivCPOffsCode]&quot;</tt> and <tt>&quot;[Code]&quot;</tt> rules in <font SIZE="-1">PDL::PP</font>.</p>
<h3>Macro access to the bad flag of a piddle</h3>
<p>Macros have been provided to provide access to the bad-flag status of a pdl: </p>
<pre> '$PDLSTATEISBAD(a)' -&gt; '($PDL(a)-&gt;state &amp; PDL_BADVAL) &gt; 0'
 '$PDLSTATEISGOOD(a)' '($PDL(a)-&gt;state &amp; PDL_BADVAL) == 0'
 '$PDLSTATESETBAD(a)' '$PDL(a)-&gt;state |= PDL_BADVAL'
 '$PDLSTATESETGOOD(a)' '$PDL(a)-&gt;state &amp;= ~PDL_BADVAL'</pre>
<p>For use in <tt>&quot;xxxxBadStatusCode&quot;</tt> (+ other stuff that goes into the <font SIZE="-1">INIT:</font> section) there are: </p>
<pre> '$SETPDLSTATEBAD(a)' -&gt; 'a-&gt;state |= PDL_BADVAL'
 '$SETPDLSTATEGOOD(a)' -&gt; 'a-&gt;state &amp;= ~PDL_BADVAL'
 '$ISPDLSTATEBAD(a)' -&gt; '((a-&gt;state &amp; PDL_BADVAL) &gt; 0)'
 '$ISPDLSTATEGOOD(a)' -&gt; '((a-&gt;state &amp; PDL_BADVAL) == 0)'</pre>
<p>In <font SIZE="-1">PDL 2.4.3</font> the <tt>&quot;$BADFLAGCACHE()&quot;</tt> macro was introduced for use in <tt>&quot;FindBadStatusCode&quot;</tt> and <tt>&quot;CopyBadStatusCode&quot;</tt>.</p>
<h3>Handling NaN values</h3>
<p>There are two issues:</p>
<dl>
<dt>NaN as the bad value</p>
<dd>which is done. To select, set <tt>&quot;BADVAL_USENAN&quot;</tt> to 1 in perldl.conf; a value of 0 falls back to treating the floating-point types the same as the integers. I need to do some benchmarks to see which is faster, and whether it&#8217;s dependent on machines (Linux seems to slow down much more than my Sparc machine in some very simple tests I did).</p>
<dt>Ignoring BadCode sections</p>
<dd>which is <i>not</i>.</dl>
<p> For <i>simple</i> routines processing floating-point numbers, we should let the computer process the bad values (i.e. <tt>&quot;NaN&quot;</tt> and <tt>&quot;Inf&quot;</tt> values) instead of using the code in the <tt>&quot;BadCode&quot;</tt> section. Many such routines have been labeled using <tt>&quot;NoBadifNaN =&gt; 1&quot;</tt>; however this is currently <i>ignored</i> by <font SIZE="-1">PDL::PP.</font> </p>
<p> For these routines, we want to use the <tt>&quot;Code&quot;</tt> section if </p>
<pre> the piddle does not have its bad flag set
 the datatype is a float or double</pre>
<p>otherwise we use the <tt>&quot;BadCode&quot;</tt> section. This is <i></i><font SIZE="-1"><i>NOT IMPLEMENTED</i></font><i></i>, as it will require reasonable hacking of PP::PDLCode! </p>
<p> There&#8217;s also the problem of how we handle &#8216;exceptions&#8217; &#8211; since <tt>&quot;$a = <a href="/docs/linux/man/2-pdl/">pdl</a>(2) / pdl(0)&quot;</tt> produces a bad value but doesn&#8217;t update the badflag value of the piddle. Can we catch an exception, or do we have to trap for this (e.g. search for <tt>&quot;exception&quot;</tt> in <i>Basic/Ops/ops.pd</i>)? </p>
<p> Checking for <tt>&quot;Nan&quot;</tt>, and <tt>&quot;Inf&quot;</tt> is done by using the <tt>&quot;finite()&quot;</tt> system call. If you want to set a value to the <tt>&quot;NaN&quot;</tt> value, the following bit of code can be used (this can be found in both <i>Basic/Core/Core.xs.PL</i> and <i>Basic/Bad/bad.pd</i>): </p>
<pre> /* for big-endian machines */
 static union { unsigned char __c[4]; float __d; } 
 __pdl_nan = { { 0x7f, 0xc0, 0, 0 } };
 /* for little-endian machines */
 static union { unsigned char __c[4]; float __d; } 
 __pdl_nan = { { 0, 0, 0xc0, 0x7f } };</pre>
<p>This approach should probably be replaced by library routines such as <tt>&quot;nan(&quot;&quot;)&quot;</tt> or <tt>&quot;atof(&quot;NaN&quot;)&quot;</tt>. </p>
<p> To find out whether a particular machine is big endian, use the routine <tt>&quot;PDL::Core::Dev::isbigendian()&quot;</tt>.</p>
<h2>What About Documentation?</h2>
<p>One of the strengths of <font SIZE="-1">PDL</font> is its on-line documentation. The aim is to use this system to provide information on how/if a routine supports bad values: in many cases <tt>&quot;pp_def()&quot;</tt> contains all the information anyway, so the function-writer doesn&#8217;t need to do anything at all! For the cases when this is not sufficient, there&#8217;s the <tt>&quot;BadDoc&quot;</tt> option. For code written at the Perl level &#8211; i.e. in a .pm file &#8211; use the <tt>&quot;=for bad&quot;</tt> pod directive. </p>
<p> This information will be available via man/pod2man/html documentation. It&#8217;s also accessible from the <tt>&quot;perldl&quot;</tt> or <tt>&quot;pdl2&quot;</tt> shells &#8211; using the <tt>&quot;badinfo&quot;</tt> command &#8211; and the <tt>&quot;pdldoc&quot;</tt> shell command &#8211; using the <tt>&quot;-b&quot;</tt> option. </p>
<p> This support is at a very early stage &#8211; i.e. not much thought has gone into it: comments are welcome; improvements to the code preferred ;) One awkward problem is for <i>*.pm</i> code: you have to write a <i>*.pm.PL</i> file which only inserts the <tt>&quot;=for bad&quot;</tt> directive (+ text) if bad value support is compiled in. In fact, this is a pain when handling bad values at the Perl, rather than <font SIZE="-1">PDL::PP,</font> level: perhaps I should just scrap the <tt>&quot;WITH_BADVAL&quot;</tt> option&#8230;</p>
<h2>Current Issues</h2>
<p>There are a number of areas that need work, user input, or both! They are mentioned elsewhere in this document, but this is just to make sure they don&#8217;t get lost.</p>
<h3>Trapping invalid mathematical operations</h3>
<p>Should we add exceptions to the functions in <tt>&quot;PDL::Ops&quot;</tt> to set the output bad for out-of-range input values? </p>
<pre> pdl&gt; p log10(pdl(10,100,-1))</pre>
<p>I would like the above to produce &#8220;[1 2 <font SIZE="-1">BAD</font>]&#8221;, but this would slow down operations on <i>all</i> piddles. We could check for <tt>&quot;NaN&quot;</tt>/<tt>&quot;Inf&quot;</tt> values after the operation, but I doubt that would be any faster.</p>
<h3>Integration with NaN</h3>
<p>When <tt>&quot;BADVAL_USENAN&quot;</tt> is true, the routines in <tt>&quot;PDL::Ops&quot;</tt> should just fall through to the <tt>&quot;Code&quot;</tt> section &#8211; i.e. don&#8217;t use <tt>&quot;BadCode&quot;</tt> &#8211; for <tt>&quot;float&quot;</tt> and <tt>&quot;double&quot;</tt> data types.</p>
<h3>Global versus per-piddle bad values</h3>
<p>I think all that&#8217;s needed is to change the routines in <tt>&quot;Basic/Core/pdlconv.c.PL&quot;</tt>, although there&#8217;s bound to be complications. It would also mean that the pdl structure would need to have a variable to store its bad value, which would mean binary incompatibility with previous versions of <font SIZE="-1">PDL</font> with bad value support. </p>
<p> As of 17 March 2006, <font SIZE="-1">PDL</font> contains the <code>experimental</code> <tt>&quot;BADVAL_PER_PDL&quot;</tt> configuration option which, if selected, adds per-piddle bad values.</p>
<h3>Dataflow of the badflag</h3>
<p>Currently changes to the bad flag are propagated to the children of a piddle, but perhaps they should also be passed on to the parents as well. With the advent of per-piddle bad values we need to consider how to handle changes to the value used to represent bad items too.</p>
<h2>Everything Else</h2>
<p>The build process has been affected. The following files are now created during the build: </p>
<pre> Basic/Core/pdlcore.h pdlcore.h.PL
 pdlcore.c pdlcore.c.PL
 pdlapi.c pdlapi.c.PL
 Core.xs Core.xs.PL
 Core.pm Core.pm.PL</pre>
<p>Several new files have been added: </p>
<pre> Basic/Pod/BadValues.pod (i.e. this file)
 t/bad.t
 Basic/Bad/
 Basic/Bad/Makefile.PL
 bad.pd</pre>
<p>etc</p>
<h2>Todo/Suggestions</h2>
<dl>
<dt>&bull;</p>
<dd>Look at using per-piddle bad values. Would mean a change to the pdl structure (i.e. binary incompatibility) and the routines in <tt>&quot;Basic/Core/pdlconv.c.PL&quot;</tt> would need changing to handle this. Most other routines <i>should not</i> need to be changed &#8230; </p>
<p> See the <code>experimental</code> <tt>&quot;BADVAL_PER_PDL&quot;</tt> option.</p>
<dt>&bull;</p>
<dd>what to do about <tt>&quot;$b = pdl(-2); $a = log10($b)&quot;</tt> &#8211; <tt>$a</tt> should be set bad, but it currently isn&#8217;t.</p>
<dt>&bull;</p>
<dd>Allow the operations in PDL::Ops to skip the check for bad values when using NaN as a bad value and processing a floating-point piddle. Needs a fair bit of work to PDL::PP::PDLCode.</p>
<dt>&bull;</p>
<dd><tt>&quot;$pdl-&gt;baddata()&quot;</tt> now updates all the children of this piddle as well. However, not sure what to do with parents, since: </p>
<pre> $b = $a-&gt;slice(); 
 $b-&gt;baddata(0)</pre>
<p>doesn&#8217;t mean that <tt>$a</tt> shouldn&#8217;t have its badvalue cleared. however, after </p>
<pre> $b-&gt;<a href="//www.systutorials.com/docs/linux/man/1-baddata/">baddata</a>(1)</pre>
<p>it&#8217;s sensible to assume that the parents now get flagged as containing bad values. </p>
<p> <font SIZE="-1">PERHAPS</font> you can only clear the bad value flag if you are <font SIZE="-1">NOT</font> a child of another piddle, whereas if you set the flag then all children <font SIZE="-1">AND</font> parents should be set as well? </p>
<p> Similarly, if you change the bad value in a piddle, should this be propagated to parent &amp; children? Or should you only be able to do this on the &#8216;top-level&#8217; piddle? Nasty&#8230;</p>
<dt>&bull;</p>
<dd>get some code set up to do benchmarks to see how much things are slowed down (and to check that I haven&#8217;t messed things up if <tt>&quot;WITH_BADVAL&quot;</tt> is 0/undef).</p>
<dt>&bull;</p>
<dd>some of the names aren&#8217;t appealing &#8211; I&#8217;m thinking of <tt>&quot;orig_badvalue()&quot;</tt> in <i>Basic/Bad/bad.pd</i> in particular. Any suggestions appreciated.</dl>
<h2>Author</h2>
<p>Copyright (C) Doug Burke (djburke [at] cpan.org), 2000, 2006. </p>
<p> The per-piddle bad value support is by Heiko Klein (2006). </p>
<p> Commercial reproduction of this documentation in a different format is forbidden.</p>
