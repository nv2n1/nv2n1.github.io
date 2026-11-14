---
title: "beakerlib-rpms(1)"
name: "beakerlib-rpms"
section: "1"
letter: "b"
url: "/docs/linux/man/1-beakerlib-rpms/"
---

<h2 class="name">NAME</h2>
 

 BeakerLib - rpms - Package manipulation helpers 

<h2>DESCRIPTION</h2>

 Functions in this BeakerLib script are used for <font SIZE="-1">RPM</font> manipulation.

<h2>FUNCTIONS</h2>

<h3>Rpm Handling</h3>

 <i>rlCheckRpm</i> 

 Check whether a package is installed. 

 <pre><code>
rlCheckRpm name[version][release][arch]
</code></pre>
<dl>
<dt>name
<dd> Package name like <tt>&quot;kernel&quot;</tt>
<dt>version
<dd> Package version like <tt>2.6.25.6</tt>
<dt>release
<dd> Package release like <tt>&quot;55.fc9&quot;</tt>
<dt>arch
<dd> Package architucture like <tt>&quot;i386&quot;</tt></dl>
 

 Returns 0 if the specified package is installed. 

 <i>rlAssertRpm</i> 

 Assertion making sure that a package is installed. 

 
rlAssertRpm name[version][release][arch] &gt;
    rlAssertRpm-- all

<dl>
<dt>name
<dd> Package name like <tt>&quot;kernel&quot;</tt>
<dt>version
<dd> Package version like <tt>2.6.25.6</tt>
<dt>release
<dd> Package release like <tt>&quot;55.fc9&quot;</tt>
<dt>arch
<dd> Package architucture like <tt>&quot;i386&quot;</tt>
<dt>--all
<dd> Assert all packages listed in the <tt>$PACKAGES</tt> <tt>$REQUIRES</tt> and <tt>$COLLECTIONS</tt> environment variables.</dl>
 

 Returns 0 and asserts <font SIZE="-1">PASS</font> if the specified package is installed. 

 <i>rlAssertNotRpm</i> 

 Assertion making sure that a package is not installed. This is just inverse of <tt>&quot;rlAssertRpm&quot;</tt>. 

 
rlAssertNotRpm name[version][release][arch] &gt;

<dl>
<dt>name
<dd> Package name like <tt>&quot;kernel&quot;</tt>
<dt>version
<dd> Package version like <tt>2.6.25.6</tt>
<dt>release
<dd> Package release like <tt>&quot;55.fc9&quot;</tt>
<dt>arch
<dd> Package architucture like <tt>&quot;i386&quot;</tt></dl>
 

 Returns 0 and asserts <font SIZE="-1">PASS</font> if the specified package is not installed. 

 <i>Example</i> 

 Function <tt>&quot;rlAssertRpm&quot;</tt> is useful especially in prepare phase where it causes abort if a package is missing, while <tt>&quot;rlCheckRpm&quot;</tt> is handy when doing something like: 

 <pre>
    if ! rlCheckRpm package; then
         yum install package
         rlAssertRpm package
    fi
</pre> 

 <i>rlAssertBinaryOrigin</i> 

 Assertion making sure that given binary is owned by (one of) the given package(s). 

 <pre><code>
rlAssertBinaryOrigin binary package[package2[...]] PACKAGES = ... rlAssertBinaryOrigin binary
</code></pre>
<dl>
<dt>binary
<dd> Binary name like <tt>&quot;ksh&quot;</tt> or <tt>&quot;/bin/ksh&quot;</tt>
<dt>package
<dd> List of packages like <tt>&quot;ksh mksh&quot;</tt>. The parameter is optional. If missing, contents of environment variable <tt>$PACKAGES</tt> are taken into account.</dl>
 

 Returns 0 and asserts <font SIZE="-1">PASS</font> if the specified binary belongs to (one of) the given package(s). Returns 1 and asserts <font SIZE="-1">FAIL</font> if the specified binary does not belong to (any of) the given package(s). Returns 2 and asserts <font SIZE="-1">FAIL</font> if the specified binary is not found. Returns 3 and asserts <font SIZE="-1">FAIL</font> if no packages are given. Returns 100 and asserts <font SIZE="-1">FAIL</font> if invoked with no parameters. 

 <i>Example</i> 

 Function <tt>&quot;rlAssertBinaryOrigin&quot;</tt> is useful especially in prepare phase where it causes abort if a binary is missing or is owned by different package: 

 <pre>
    PACKAGES=mksh rlAssertBinaryOrigin ksh
    or
    rlAssertBinaryOrigin ksh mksh
</pre> 

 Returns true if ksh is owned by the mksh package (in this case: /bin/ksh is a symlink pointing to /bin/mksh). 

 <i>rlGetMakefileRequires</i> 

 Prints comma separated list of requirements defined in Makefile using 'Requires' attribute. 

 Return 0 if success. 

 <i>rlCheckRequirements</i> 

 Check that all given requirements are covered eigther by installed package or by binary available in PATHs or by some package's provides. 

 <pre>
    rlRun &quot;rlCheckRequirements REQ...&quot;
</pre>
<dl>
<dt><font SIZE="-1">REQ</font>
<dd> Requirement to be checked. It can be package name, provides string or binary name.</dl>
 

 Returns number of unsatisfied requirements. 

 <i>rlCheckMakefileRequires</i> 

 This is just a bit smarted wrapper of 

 <tt>&quot;rlCheckRequirements $(rlGetMakefileRequires)&quot;</tt> 

 <i>Example</i> 

 <pre>
    rlRun &quot;rlCheckMakefileRequires&quot;
</pre> 

 Return 255 if requirements could not be retrieved, 0 if all requirements are satisfied or number of unsatisfied requirements.

<h2>AUTHORS</h2>

<dl>
<dt>&bull;
<dd> Petr Muller &lt;pmuller [at] redhat.com&gt;
<dt>&bull;
<dd> Jan Hutar &lt;jhutar [at] redhat.com&gt;
<dt>&bull;
<dd> Petr Splichal &lt;psplicha [at] redhat.com&gt;
<dt>&bull;
<dd> Ales Zelinka &lt;azelinka [at] redhat.com&gt;
<dt>&bull;
<dd> Dalibor Pospisil &lt;dapospis [at] redhat.com&gt; 

</dl>

<h2>Index</h2>


