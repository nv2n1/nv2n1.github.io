---
title: "quvi-modules(7)"
name: "quvi-modules"
section: "7"
letter: "q"
url: "/docs/linux/man/7-quvi-modules/"
description: "quvi-modules – Overview of the loadable quvi modules"
---

<p>quvi-modules &#8211; Overview of the loadable quvi modules</p>
<h2>Description</h2>
<p><i>quvi-modules</i> are a selection of importable modules implemented in Lua. These modules are intended to be loaded (<i>require</i>) from the <code><a href="/docs/linux/man/7-libquvi-scripts/">libquvi-scripts</a></code>(7). </p>
<p> Many of the modules are documented within the code. Refer to the individual modules for their detailed description of different available functions. </p>
<p> The modules are usually installed at</p>
<dl>
<dd>$prefix/share/libquvi-scripts/$major_ver.$minor_ver/common/quvi/</dl>
<h2>Modules</h2>
<p>quvi/http/cookie</p>
<dl>
<dd>A set of functions that wrap most of the quvi.http.cookie function features. See <code><a href="/docs/linux/man/7-quvi-object/">quvi-object</a></code>(7).</dl>
<p> quvi/const</p>
<dl>
<dd>Constants. Technically, (due to Lua language specification) these are not immutable values. The <i>constants</i> are used to interact with libquvi, e.g. specifying function operation modes and checking for returned libquvi return codes.</dl>
<p> quvi/debug</p>
<dl>
<dd>An message output facility intended to be used for debugging purposes. By <i>default</i>, all output from scripts using this facility remain <i>disabled</i>. To enable the output, define the LIBQUVI_SCRIPTS_VERBOSE environment variable.</dl>
<p> quvi/entity</p>
<dl>
<dd>HTML entity conversion module. Converts the <i>standard HTML entities</i> (to ASCII), and any numeric HTML entities to UTF-8 (using the <i>quvi/html</i> module).</dl>
<p> quvi/hash</p>
<dl>
<dd>Wrapper functions for some of the common hash (message digest) functions provided by the <code><a href="/docs/linux/man/7-quvi-object/">quvi-object</a></code>(7). Note that these functions convert the given data into hexadecimal form before passing it to the hash functions.</dl>
<p> quvi/hex</p>
<dl>
<dd>Functions for converting values from and to hexadecimal form. These are typically used together with the <code><a href="/docs/linux/man/7-quvi-object/">quvi-object</a></code>(7) crypto functions.</dl>
<p> quvi/html</p>
<dl>
<dd>Converts numeric HTML entities to UTF-8. See also <i>quvi/entity</i>, which uses this module.</dl>
<p> quvi/lxph</p>
<dl>
<dd>LuaExpat wrapper/utility functions for parsing XML, see also <code><a href="/docs/linux/man/7-quvi-modules-3rdparty/">quvi-modules-3rdparty</a></code>(7).</dl>
<p> quvi/stream</p>
<dl>
<dd>Media stream related functions.</dl>
<p> quvi/time</p>
<dl>
<dd>Time related functions.</dl>
<p> quvi/util</p>
<dl>
<dd>Misc. utility functions.</dl>
<p> quvi/youtube</p>
<dl>
<dd>Functions common to YouTube.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-libquvi-scripts/">libquvi-scripts</a></code>(7), <code><a href="/docs/linux/man/3-libquvi/">libquvi</a></code>(3), <code><a href="/docs/linux/man/7-quvi-object/">quvi-object</a></code>(7), <code><a href="/docs/linux/man/7-quvi-modules-3rdparty/">quvi-modules-3rdparty</a></code>(7)</p>
<h2>Further Resources</h2>
<p>Home</p>
<dl>
<dd><a rel="nofollow" href="http://quvi.sourceforge.net/">http://quvi.sourceforge.net/</a></dl>
<p> Development code</p>
<dl>
<dd><a href="git://repo.or.cz/libquvi-scripts.git">git://repo.or.cz/libquvi-scripts.git</a></dl>
<p> gitweb</p>
<dl>
<dd><a rel="nofollow" href="http://repo.or.cz/w/libquvi-scripts.git">http://repo.or.cz/w/libquvi-scripts.git</a></dl>
<h2>Authors</h2>
<p>Toni Gundogdu &lt;legatvs [at] gmail.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to the quvi-devel mailing list &lt;quvi-devel [at] lists.sourceforge.net&gt; where the development and the maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>License</h2>
<p>libquvi-scripts is Free Software licensed under the GNU Affero GPLv3+</p>
<h2>Libquvi-Scripts</h2>
<p>Part of the <i><a href="/docs/linux/man/7-libquvi-scripts/">libquvi-scripts</a>(7)</i> suite</p>
