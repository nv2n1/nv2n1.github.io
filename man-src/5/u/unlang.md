---
title: "unlang(5)"
name: "unlang"
section: "5"
letter: "u"
url: "/docs/linux/man/5-unlang/"
description: "unlang – FreeRADIUS Processing un-language"
---

<p>unlang &#8211; FreeRADIUS Processing un-language</p>
<h2>Description</h2>
<p>FreeRADIUS supports a simple processing language in its configuration files. We call it an &quot;un-language&quot; because the intention is NOT to create yet another programming language. If you need something more complicated than what is described here, we suggest using the Perl or Python modules rlm_perl, or rlm_python. </p>
<p> The goal of the language is to allow simple policies to be written with minimal effort. Those policies are then applied when a request is being processed. Requests are processed through virtual servers (including the default one), in the sections titled &quot;authorize&quot;, &quot;authenticate&quot;, &quot;post-auth&quot;, &quot;preacct&quot;, &quot;accounting&quot;, &quot;pre-proxy&quot;, &quot;post-proxy&quot;, and &quot;session&quot;. </p>
<p> These policies cannot be used in any other part of the configuration files, such as module or client configuration.</p>
<h2>Keywords</h2>
<p>The keywords for the language are a combination of pre-defined keywords, and references to loadable module names. We document only the pre-defined keywords here. </p>
<p> Subject to a few limitations described below, any keyword can appear in any context. The language consists of a series of entries, each one one line. Each entry begins with a keyword. Entries are organized into lists. Processing of the language is line by line, from the start of the list to the end. Actions are executed per-keyword.</p>
<dl>
<dt>module-name</p>
<dd>A reference to the named module. When processing reaches this point, the pre-compiled module is called. The module may succeed or fail, and will return a status to &quot;unlang&quot; if so. This status can be tested in a condition. See the &quot;Simple Conditions&quot; text in the CONDITIONS section, and MODULE RETURN CODES, below. </p>
<dl>
<dd>
<pre> chap # call the CHAP module
<br>
 sql # call the SQL module
<br>
 ...</pre>
</dl>
<dt>if</p>
<dd>Checks for a particular condition. If true, the block after the condition is processed. Otherwise, the block is ignored. See CONDITIONS, below, for documentation on the format of the conditions. </p>
<dl>
<dd>
<pre> if (condition) {
<br>
 ...
<br>
 }</pre>
</dl>
<dt>else</p>
<dd>Define a block to be executed only if the previous &quot;if&quot; condition returned false. </p>
<dl>
<dd>
<pre> else {
<br>
 ...
<br>
 }</pre>
</dl>
<dt>elsif</p>
<dd>Define a block to be executed only if the previous &quot;if&quot; condition returned false, and if the specified condition evaluates to true. </p>
<dl>
<dd>
<pre> elsif (condition) {
<br>
 ...
<br>
 }</pre>
</dl>
<dt>foreach</p>
<dd>Loops over values of an attribute, running the block for each value. The return value of the block is the return value of the last statement executed. The loop can be exited early by using the &quot;break&quot; keyword. Unlike other languages, &quot;break&quot; here means &quot;exit the loop at the next iteration&quot;, not &quot;exit the loop now&quot;. The result is that any statements after the &quot;break&quot; keyword will still be executed. We recommend using &quot;break&quot; only when it is the last statement in a &quot;foreach&quot; block. </p>
<p> Inside of the &quot;foreach&quot; block, the attribute which is being looped over can be referenced as &quot;Foreach-Variable-#&quot;. Where &quot;#&quot; is the depth of the loop, starting at &quot;0&quot;. e.g. &quot;Foreach-Variable-0&quot;. The loops can be nested up to eight (8) deep, though this is not recommended. </p>
<dl>
<dd>
<pre> foreach &amp;Attribute-Reference {
<br>
 ...
<br>
 }</pre>
</dl>
<dt>switch</p>
<dd>A &quot;switch&quot; statement takes one argument, and contains a series of &quot;case&quot; statements. When a &quot;switch&quot; statement is encountered, the argument from the &quot;switch&quot; is evaluated in turn against the argument from each &quot;case&quot; statement. The first &quot;case&quot; statement which matches is executed. All other &quot;case&quot; statements are ignored. A default &quot;case&quot; statement can be defined, by omitting its argument. </p>
<p> If the argument is a double quoted string (e.g. &quot;%{exec:1 + 2}&quot;, it is expanded as described in the DATA TYPES section, below. The match is then performed on the string returned from the expansion. If the argument is an attribute reference (e.g. &amp;User-Name), then the match is performed on the value of that attribute. Otherwise, the argument is taken to be a literal string, and and matching is done via simple comparison. </p>
<p> No statement other than &quot;case&quot; can appear in a &quot;switch&quot; block. </p>
<dl>
<dd>
<pre> switch &lt;argument&gt; {
<br>
 ...
<br>
 }</pre>
</dl>
<dt>case</p>
<dd>Provides a place-holder which matches the argument of a parent &quot;switch&quot; statment. </p>
<p> A &quot;case&quot; statement cannot appear outside of a &quot;switch&quot; block. </p>
<p> If the argument is a double quoted string (e.g. &quot;%{exec:1 + 2}&quot;, it is expanded as described in the DATA TYPES section, below. The match is then performed on the string returned from the expansion. If the argument is an attribute reference (e.g. &amp;User-Name), then the match is performed on the value of that attribute. Otherwise, the argument is taken to be a literal string, and and matching is done via simple comparison. </p>
<dl>
<dd>
<pre> case &lt;argument&gt; {
<br>
 ...
<br>
 }</pre>
</dl>
<p> A default entry can be defined by omitting the argument, as given below. This entry will be used if no other &quot;case&quot; entry matches. Only one default entry can exist in a &quot;switch&quot; section. </p>
<dl>
<dd>
<pre> case {
<br>
 ...
<br>
 }</pre>
</dl>
<dt>update</p>
<dd>Update a particular attribute list, based on the attributes given in the current block. </p>
<dl>
<dd>
<pre> update &lt;list&gt; {
<br>
 Attribute-Reference = value
<br>
 ...
<br>
 }</pre>
</dl>
<p> The &lt;list&gt; can be one of &quot;request&quot;, &quot;reply&quot;, &quot;proxy-request&quot;, &quot;proxy-reply&quot;, &quot;coa&quot;, &quot;disconnect&quot;, or &quot;control&quot;. As of Version 3, the &lt;list&gt; can be omitted, in which case &quot;request&quot; is assumed. </p>
<p> The &quot;control&quot; list is the list of attributes maintainted internally by the server that controls how the server processes the request. Any attribute that does not go in a packet on the network will generally be placed in the &quot;control&quot; list. </p>
<p> For EAP methods with tunneled authentication sessions (i.e. PEAP and EAP-TTLS), the inner tunnel session can also reference &quot;outer.request&quot;, &quot;outer.reply&quot;, and &quot;outer.control&quot;. Those references allow you to address the relevant list in the outer tunnel session. </p>
<p> The &quot;coa&quot; and &quot;disconnect&quot; sections can only be used when the server receives an Access-Request or Accounting-Request. Use &quot;request&quot; and &quot;reply&quot; instead of &quot;coa&quot; when the server receives a CoA-Request or Disconnect-Request packet. </p>
<p> Adding one or more attributes to either of the &quot;coa&quot; or &quot;disconnect&quot; list causes server to originate a CoA-Request or Disconnect-Request packet. That packet is sent when the current Access-Request or Accounting-Request has been finished, and a reply sent to the NAS. See raddb/sites-available/originate-coa for additional information. </p>
<p> The only contents permitted in an &quot;update&quot; section are attributes and values. The contents of the &quot;update&quot; section are described in the ATTRIBUTE REFERENCE and ATTRIBUTE ASSIGNMENT sections below.</p>
<dt>redundant</p>
<dd>This section contains a simple list of modules. The first module is called when the section is being processed. If the first module succeeds in its operation, then the server stops processing the section, and returns to the parent section. </p>
<p> If, however, the module fails, then the next module in the list is tried, as described above. The processing continues until one module succeeds, or until the list has been exhausted. </p>
<p> Redundant sections can contain only a list of modules, and cannot contain keywords that perform conditional operations (if, else, etc) or update an attribute list. </p>
<dl>
<dd>
<pre> redundant {
<br>
 sql1 # try this
<br>
 sql2 # try this only if sql1 fails.
<br>
 ...
<br>
 }</pre>
</dl>
<dt>load-balance</p>
<dd>This section contains a simple list of modules. When the section is entered, one module is chosen at random to process the request. All of the modules in the list should be the same type (e.g. ldap or sql). All of the modules in the list should behave identically, otherwise the load-balance section will return different results for the same request. </p>
<p> Load-balance sections can contain only a list of modules, and cannot contain keywords that perform conditional operations (if, else, etc) or update an attribute list. </p>
<dl>
<dd>
<pre> load-balance {
<br>
 ldap1 # 50% of requests go here
<br>
 ldap2 # 50% of requests go here
<br>
 }</pre>
</dl>
<p> In general, we recommend using &quot;redundant-load-balance&quot; instead of &quot;load-balance&quot;.</p>
<dt>redundant-load-balance</p>
<dd>This section contains a simple list of modules. When the section is entered, one module is chosen at random to process the request. If that module succeeds, then the server stops processing the section. If, however, the module fails, then one of the remaining modules is chosen at random to process the request. This process repeats until one module succeeds, or until the list has been exhausted. </p>
<p> All of the modules in the list should be the same type (e.g. ldap or sql). All of the modules in the list should behave identically, otherwise the load-balance section will return different results for the same request. </p>
<p> Load-balance sections can contain only a list of modules, and cannot contain keywords that perform conditional operations (if, else, etc) or update an attribute list. </p>
<dl>
<dd>
<pre> redundant-load-balance {
<br>
 ldap1 # 50%, unless ldap2 is down, then 100%
<br>
 ldap2 # 50%, unless ldap1 is down, then 100%
<br>
 }</pre>
</dl>
</dl>
<h2>Attribute References</h2>
<p>Attributes may be referenced via the following syntax:</p>
<dl>
<dd>
<pre> Attribute-Name
 Attribute-Name:TAG
 Attribute-Name[NUM]
 &lt;list&gt;:Attribute-Name
 &lt;list&gt;:Attribute-Name:TAG[NUM]</pre>
</dl>
<p> Where &lt;list&gt; is one of &quot;request&quot;, &quot;reply&quot;, &quot;control&quot;, &quot;proxy-request&quot;, &quot;proxy-reply&quot;, or &quot;outer.request&quot;, &quot;outer.reply&quot;, &quot;outer.control&quot;, &quot;outer.proxy-request&quot;, or &quot;outer.proxy-reply&quot;. just as with the &quot;update&quot; section, above. The &quot;&lt;list&gt;:&quot; prefix is optional, and if omitted, is assumed to refer to the &quot;request&quot; list. </p>
<p> The TAG portion is a decimal integer between 1 and 31. Please see RFC 2868 for more information about tags. Tags can only be used for attributes which are marked in the dictionary as &quot;has_tag&quot;. </p>
<p> The NUM portion is used when there are multiple attributes of the same name in a list. The &quot;Attribute-Name&quot; reference will return the first attribute. Using an array offset allows the policy to refer to the second and subsequent attributes. </p>
<p> When an attribute name is encountered, the given list is examined for an attribute of the given name. Some examples are:</p>
<dl>
<dd>
<pre> User-Name
<br>
 request:User-Name # same as above
<br>
 reply:User-Name
<br>
 Tunnel-Password:1
<br>
 Cisco-AVPAir[2]
<br>
 outer.request:User-Name # from inside of a TTLS/PEAP tunnel</pre>
</dl>
<p> Note that unlike C, there is no way to define new attributes at run-time. They MUST be declared in a dictionary file, and loaded when the server starts. </p>
<p> All attributes are defined in the dictionaries that accompany the server. These definitions define only the name and type, and do not define the value of the attribute. When the server receives a packet, it uses the packet contents to look up entries in the dictionary, and instantiates attributes with a name taken from the dictionaries, and a value taken from the packet contents. This process means that if an attribute does not exist, it is usually because it was not contained in a packet that the server received. </p>
<p> Once the attribute is instantiated, it is added to a list. It can then be referenced, updated, replaced, etc.</p>
<h2>Conditions</h2>
<p>The conditions are similar to C conditions in syntax, though quoted strings are supported, as with the Unix shell.</p>
<dl>
<dt>Simple</p>
<dd>conditions </p>
<dl>
<dd>
<pre> (foo)</pre>
</dl>
<p> Evalutes to true if &#8216;foo&#8217; is a non-empty string (single quotes, double quotes, or back-quoted). Also evaluates to true if &#8216;foo&#8217; is a non-zero number. Note that the language is poorly typed, so the string &quot;0000&quot; can be interpreted as a numerical zero. This issue can be avoided by comparings strings to an empty string, rather than by evaluating the string by itself. </p>
<p> If the word &#8216;foo&#8217; is not a quoted string, then it can be taken as a reference to a named attribute. See &quot;Referencing attribute lists&quot;, below, for examples of attribute references. The condition evaluates to true if the named attribute exists. </p>
<p> Otherwise, if the word &#8216;foo&#8217; is not a quoted string, and is not an attribute reference, then it is interpreted as a reference to a module return code. The condition evaluates to true if the most recent module return code matches the name given here. Valid module return codes are given in MODULE RETURN CODES, below.</p>
<dt>Negation</p>
<dd>
<dl>
<dd>
<pre> (!foo)</pre>
</dl>
<p> Evalutes to true if &#8216;foo&#8217; evaluates to false, and vice-versa.</dl>
<p> Short-circuit operators</p>
<dl>
<dd>
<dl>
<dd>
<pre> (foo || bar)
<br>
 (foo &amp;&amp; bar)</pre>
</dl>
<p> &quot;&amp;&amp;&quot; and &quot;||&quot; are short-circuit operators. &quot;&amp;&amp;&quot; evaluates the first condition, and evaluates the second condition if and only if the result of the first condition is true. &quot;||&quot; is similar, but executes the second command if and only if the result of the first condition is false.</dl>
<dl>
<dt>Comparisons</p>
<dd>
<dl>
<dd>
<pre> (foo == bar)</pre>
</dl>
<p> Compares &#8216;foo&#8217; to &#8216;bar&#8217;, and evaluates to true if the comparison holds true. Valid comparison operators are &quot;==&quot;, &quot;!=&quot;, &quot;&lt;&quot;, &quot;&lt;=&quot;, &quot;&gt;&quot;, &quot;&gt;=&quot;, &quot;=~&quot;, and &quot;!~&quot;, all with their usual meanings. Invalid comparison operators are &quot;:=&quot; and &quot;=&quot;.</p>
<dt>Attribute</p>
<dd>
<dl>
<dd>
<pre> (User-Name == &quot;foo&quot;)</pre>
</dl>
<p> Compares the value of the User-Name attribute to the string &#8216;foo&#8217;, and evaluates to true if the comparison holds true. The comparison is done by printing the attribute to a string, and then doing a string comparison of the two sides of the condition.</p>
<dt>Inter-Attribute</p>
<dd>
<dl>
<dd>
<pre> (User-Name == &amp;Filter-Id)</pre>
</dl>
<p> Compares the value of the User-Name attribute to the contents of the Filter-Id attribute, and evaluates to true if the comparison holds true. Unlike the previous example, this comparison is done in a type-safe way. For example, comparing the IP addresses 1.2.3.4 and 127.0.0.1 as strings will return different results than comparing them as IP addresses. </p>
<p> The &quot;&amp;&quot; character in the condition means that the comparison &quot;refers&quot; to the Filter-Id attribute. If left off, it means that the User-Name attribute is compared to the literal string &quot;Filter-Id&quot;. </p>
<p> Where the left-hand side is an attribute, the &quot;&amp;&quot; can be omitted. However, it is allowed for completeness. e.g. The comparison &quot;(&amp;User-Name == &amp;Filter-Id)&quot; is equivalent to the example above. </p>
<p> We recommend using attribute references instead of printing attributes to a string, via (User-Name == &quot;%{Filter-Id}&quot;). Attribute references will be faster and more efficient. </p>
<dt>Casts</p>
<dd>
<dl>
<dd>
<pre> (&lt;type&gt;foo == bar)</pre>
</dl>
<p> The left-hand-side of a condition can be &quot;cast&quot; to a specific data type. The data type must be one which is valid for the dictionaries. e.g. &quot;integer&quot;, &quot;ipaddr&quot;, etc. </p>
<p> The comparison is performed in a type-safe way, as with &quot;Inter-Attribute Comparisons&quot;, above. Both sides of the condition are parsed into temporary attributes, and the attributes compared via type-specific methods. The temporary attributes have no other effect, and are not saved anywhere. </p>
<p> Casting allows conditions to perform type-specific comparisons. In previous versions of the server, the data would have to be manually placed into an intermediate attribute (or attributes), and then the attribute (or attributes) compared. The use of a cast allows for simpler policies. </p>
<p> Casts are allowed only on the left-hand side argument of a condition.</dl>
<p> Conditions may be nested to any depth, subject only to line length limitations (8192 bytes).</p>
<h2>Data Types</h2>
<p>There are only a few data types supported in the language. Reference to attributes, numbers, and strings. Any data type can appear in stand-alone condition, in which case they are evaluated as described in &quot;Simple conditions&quot;, above. They can also appear (with some exceptions noted below) on the left-hand or on the right-hand side of a comparison.</p>
<dl>
<dt>numbers</p>
<dd>Numbers are composed of decimal digits. Floating point, hex, and octal numbers are not supported. The maximum value for a number is machine-dependent, but is usually 32-bits, including one bit for a sign value.</dl>
<p> word</p>
<dl>
<dd>Text that is not enclosed in quotes is interpreted differently depending on where it occurs in a condition. On the left hand side of a condition, it is interpreted as a reference to an attribute. On the right hand side, it is interpreted as a simple string, in the same manner as a single-quoted string. </p>
<p> Using attribute references permits limited type-specific comparisons, as seen in the examples below. </p>
<dl>
<dd>
<pre> if (User-Name == &quot;bob&quot;) {
<br>
 ...
<br>
 if (Framed-IP-Address &gt; 127.0.0.1) {
<br>
 ...
<br>
 if (Service-Type == Login-User) { </pre>
</dl>
</dl>
<dl>
<dt>&quot;strings&quot;</p>
<dd>
<dl>
<dd>Double-quoted strings are expanded by inserting the value of any attributes (see VARIABLES, below) before being evaluated. If the result is a number it is evaluated in a numerical context. </p>
<p> String length is limited by line-length, usually about 8000 characters. A double quote character can be used in a string via the normal back-slash escaping method. (&quot;like \&quot;this\&quot; !&quot;)</dl>
<dt>&#8216;strings&#8217;</p>
<dd>Single-quoted strings are evaluated as-is. Their values are not expanded as with double-quoted strings above, and they are not interpreted as attribute references.</p>
<dt>`strings`</p>
<dd>Back-quoted strings are evaluated by expanding the contents of the string, as described above for double-quoted strings. The resulting command given inside of the string in a sub-shell, and taking the output as a string. This behavior is much the same as that of Unix shells. </p>
<p> Note that for security reasons, the input string is split into command and arguments before string expansion is done. </p>
<p> For performance reasons, we suggest that the use of back-quoted strings be kept to a minimum. Executing external programs is relatively expensive, and executing a large number of programs for every request can quickly use all of the CPU time in a server. If you believe that you need to execute many programs, we suggest finding alternative ways to achieve the same result. In some cases, using a real language may be sufficient.</p>
<dt>/regex/i</p>
<dd>These strings are valid only on the right-hand side of a comparison, and then only when the comparison operator is &quot;=~&quot; or &quot;!~&quot;. They are regular expressions, as implemented by the local regular expression library on the system. This is usually Posix regular expressions. </p>
<p> The trailing &#8216;i&#8217; is optional, and indicates that the regular expression match should be done in a case-insensitive fashion. </p>
<p> If the comparison operator is &quot;=~&quot;, then parantheses in the regular expression will define variables containing the matching text, as described below in the VARIABLES section.</dl>
<h2>Expansions</h2>
<p>Attributes are expanded using the ATTRIBUTE REFERENCE syntax described above, and surrounding the reference with &quot;%{&#8230;}&quot; </p>
<dl>
<dd>
<pre> %{Attribute-Reference}</pre>
</dl>
<p> The result will be a string which contains the value of the attribute which was referenced, as a printable string. If the attribute does not exist, the result will be an empty string. </p>
<p> Results of regular expression matches</p>
<dl>
<dd>If a regular expression match has previously been performed, then the special variable %{0} will contain a copy of the input string. The variables %{1} through %{8} will contain the substring matches, starting from the left-most parantheses, and onwards. If there are more than 8 parantheses, the additional results will not be placed into any variables.</dl>
<p> Obtaining results from databases</p>
<dl>
<dd>It is useful to query a database for some information, and to use the result in a condition. The following syntax will call a module, pass it the given string, and replace the string expansion with the resulting string returned from the module. </p>
<dl>
<dd>
<pre> %{module: string ...}</pre>
</dl>
<p> The syntax of the string is module-specific. Please read the module documentation for additional details.</dl>
<p> Conditional Syntax</p>
<dl>
<dd>Conditional syntax similar to that used in Unix shells may also be used.</p>
<dl>
<dt>%{%{Foo}:-bar}</p>
<dd>If %{Foo} has a value, returns that value.<br />
 Otherwise, returns literal string &quot;bar&quot;.</p>
<dt>%{%{Foo}:-%{Bar}}</p>
<dd>If %{Foo} has a value, returns that value.<br />
 Otherwise, returns the expansion of %{Bar}. </p>
<p> These conditional expansions can be nested to almost any depth, such as with %{%{One}:-%{%{Two}:-%{Three}}}</dl>
</dl>
<p> String lengths and arrays</p>
<dl>
<dd>Similar to a Unix shell, there are ways to reference string lenths, and the second or more instance of an attribute in a list. If you need more than this functionality, we suggest using a real language.</p>
<dl>
<dt>%{strlen:string}</p>
<dd>The number of characters in &quot;string&quot;. If &quot;string&quot; does not exist, then the length also does not exist, instead of being zero. </p>
<p> The &quot;string&quot; is expanded before the length is taken. </p>
<dt>%{integer:Attribute-Name}</p>
<dd>The integer value of the Attribute-Name, instead of the enumerated name. </p>
<p> e.g. If a request contains &quot;Service-Type = Login-User&quot;, the expansion of %{integer:Service-Type} will yeild &quot;1&quot;. </p>
<dt>%{hex:Attribute-Name}</p>
<dd>The hex value of the Attribute-Name, as a series of hex digits. </p>
<p> e.g. If a request contains &quot;Framed-IP-Address = 127.0.0.1&quot;, the expansion of %{hex:Framed-IP-Address} will yeild &quot;0x7f000001&quot;. </p>
</dl>
</dl>
<h2>Attribute Assignments</h2>
<p>The attribute lists described above may be edited by listing one or more attributes in an &quot;update&quot; section. Once the attributes have been defined, they may be referenced as described above in the VARIABLES section. </p>
<p> The following syntax defines attributes in an &quot;update&quot; section. Each attribute and value has to be all on one line in the configuration file. There is no need for commas or semi-colons after the value. </p>
<dl>
<dd>
<pre> Attribute-Reference = value</pre>
</dl>
<p> Attribute Reference</p>
<dl>
<dd>The Attribute-Reference must be a reference (see above), using a name previously defined in a dictionary. If an undefined name is used, the server will return an error, and will not start. </p>
</dl>
<dl>
<dt>Operators</p>
<dd>The operator used to assign the value of the attribute may be one of the following, with the given meaning.</p>
<dl>
<dd>
<dl>
<dt>=</p>
<dd>Add the attribute to the list, if and only if an attribute of the same name is not already present in that list.</p>
<dt>:=</p>
<dd>Add the attribute to the list. If any attribute of the same name is already present in that list, its value is replaced with the value of the current attribute.</p>
<dt>+=</p>
<dd>Add the attribute to the tail of the list, even if attributes of the same name are already present in the list.</dl>
</dl>
</dl>
<p> Enforcement and Filtering Operators</p>
<dl>
<dd>The following operators may also be used in addition to the ones listed above. Their function is to perform enforcement or filtering on attributes in a list.</p>
<dl>
<dt>-=</p>
<dd>Remove all matching attributes from the list. Both the attribute name and value have to match in order for the attribute to be removed from the list.</p>
<dt>==</p>
<dd>Keep all matching attributes. Both the attribute name and value have to match in order for the attribute to remain in the list. </p>
<p> Note that this operator is very different than the &#8216;=&#8217; operator listed above!</p>
<dt>&lt;=</p>
<dd>Keep all attributes having values less than, or equal to, the value given here. Any larger value is replaced by the value given here. If no attribute exists, it is added with the value given here, as with &quot;+=&quot;. </p>
<p> This operator is valid only for attributes of integer type.</p>
<dt>&gt;=</p>
<dd>Keep all attributes having values greater than, or equal to, the value given here. Any larger value is replaced by the value given here. If no attribute exists, it is added with the value given here, as with &quot;+=&quot;. </p>
<p> This operator is valid only for attributes of integer type.</p>
<dt>!*</p>
<dd>Delete all occurances of the named attribute, no matter what the value.</dl>
</dl>
<dl>
<dt>Values</p>
<dd>The value can be an attribute reference, or an attribute-specific string. </p>
<p> When the value is an an attribute reference, it must take the form of &quot;&amp;Attribute-Name&quot;. The leading &quot;&amp;&quot; signifies that the value is a reference. The &quot;Attribute-Name&quot; is an attribute name, such as &quot;User-Name&quot; or &quot;request:User-Name&quot;. When an attribute reference is used, both attributes must have the same data type. For example, &quot;User-Name := &amp;NAS-Port&quot; is invalid, because &quot;User-Name&quot; is a string, and &quot;NAS-Port&quot; is an integer. </p>
<p> We recommend using the form &quot;Attribute-1 = &amp;Attribute-2&quot; for updates, instead of &quot;Attribute-1 = &quot;%{Attribute-2}&quot;. The first version will copy the attribute data, no matter what its form. The second version will print the Attribute-2 to a string, and then parse it to create the value for Attribute-1. This second version is slower and more fragile than the first one. </p>
<p> When the value is an attribute-specific string, it can be a string, integer, IP address, etc. The value may be expanded as described above in the DATA TYPES section, above. For example, specifying &quot;Framed-IP-Address = 127.0.0.1&quot; will cause the &quot;Framed-IP-Address&quot; attribute to be set to the IP address &quot;127.0.0.1&quot;. However, using &quot;Framed-IP-Address := module to be run with a string &quot;127.0.0.1&quot;. The output of the &quot;echo&quot; module will then be parsed as an IP address, and placed into the Framed-IP-Address attribute. </p>
<p> This flexibility means that you can assign an IP address by specifying it directly, or by having the address returned from a database query, or by having the address returned as the output of a program that is executed. </p>
<p> When string values are finally assigned to an attribute, they can have a maximum length of 253 characters. This limit is due in part to both protocol and internal server requirements. That is, the strings in the language can be nearly 8k in length, say for a long SQL query. However, the output of that SQL query should be no more than 253 characters in length.</dl>
<h2>Other Keywords</h2>
<p>Other keywords in the language are taken from the names of modules loaded by the server. These keywords are dependent on both the modules, and the local configuration. </p>
<p> Some use keywords that are defined in the default configuration file are:</p>
<dl>
<dt>fail</p>
<dd>Cause the request to be treated as if a database failure had occurred.</p>
<dt>noop</p>
<dd>Do nothing. This also serves as an instruction to the configurable failover tracking that nothing was done in the current section.</p>
<dt>ok</p>
<dd>Instructs the server that the request was processed properly. This keyword can be used to over-ride earlier failures, if the local administrator determines that the faiures are not catastrophic.</p>
<dt>reject</p>
<dd>Causes the request to be immediately rejected</dl>
<h2>Module Return Codes</h2>
<p>When a module is called, it returns one of the following codes to &quot;unlang&quot;, with the following meaning. </p>
<dl>
<dd>
<pre> notfound information was not found
<br>
 noop the module did nothing
<br>
 ok the module succeeded
<br>
 updated the module updated the request
<br>
 fail the module failed
<br>
 reject the module rejected the request
<br>
 userlock the user was locked out
<br>
 invalid the configuration was invalid
<br>
 handled the module has handled the request itself</pre>
</dl>
<p> These return codes can be tested for in a condition, as described above in the CONDITIONS section. </p>
<p> See also the file doc/configurable_failover for additional methods of trapping and modifying module return codes.</p>
<h2>Files</h2>
<p>/etc/raddb/radiusd.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5), <code><a href="/docs/linux/man/5-dictionary/">dictionary</a></code>(5)</p>
<h2>Author</h2>
<p>Alan DeKok &lt;aland [at] deployingradius.com&gt;</p>
