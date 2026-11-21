---
title: "locale(1)"
name: "locale"
section: "1"
letter: "l"
url: "/docs/linux/man/1-locale/"
description: "locale – get locale-specific information"
---

<h2>SYNOPSIS</h2>
<pre><code>
locale[option] locale[option] - a locale[option] - m locale[option] name...
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>locale</code> command displays information about the current locale, or all locales, on standard output. </p>
<p> When invoked without arguments, <code>locale</code> displays the current locale settings for each locale category (see <code><a href="/docs/linux/man/5-locale/">locale</a></code>(5)), based on the settings of the environment variables that control the locale (see <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7)). Values for variables set in the environment are printed without double quotes, implied values are printed with double quotes. </p>
<p> If either the <code>-a</code> or the <code>-m</code> option (or one of their long-format equivalents) is specified, the behavior is as follows:</p>
<dl>
<dt><code>-a</code>, <code>&#8211;all-locales</code></dt>
<dd> Display a list of all available locales. The <code>-v</code> option causes the <code>LC_IDENTIFICATION</code> metadata about each locale to be included in the output.</dd>
<dt><code>-m</code>, <code>&#8211;charmaps</code></dt>
<dd> Display the available charmaps (character set description files). To display the current character set for the locale, use <code>locale -c charmap</code>.</dd></dl>
<p> The <code>locale</code> command can also be provided with one or more arguments, which are the names of locale keywords (for example, <i>date_fmt</i>, <i>ctype-class-names</i>, <i>yesexpr</i>, or <i>decimal_point</i>) or locale categories (for example, <code>LC_CTYPE</code> or <code>LC_TIME</code>). For each argument, the following is displayed:</p>
<dl>
<dt>*</dt>
<dd> For a locale keyword, the value of that keyword to be displayed.</dd>
<dt>*</dt>
<dd> For a locale category, the values of all keywords in that category are displayed.</dd></dl>
<p> When arguments are supplied, the following options are meaningful:</p>
<dl>
<dt><code>-c</code>, <code>&#8211;category-name</code></dt>
<dd> For a category name argument, write the name of the locale category on a separate line preceding the list of keyword values for that category.</dd>
<dt>
</dt><dd> For a keyword name argument, write the name of the locale category for this keyword on a separate line preceding the keyword value.</dd>
<dt>
</dt><dd> This option improves readability when multiple name arguments are specified. It can be combined with the <code>-k</code> option.</dd>
<dt><code>-k</code>, <code>&#8211;keyword-name</code></dt>
<dd> For each keyword whose value is being displayed, include also the name of that keyword, so that the output has the format:</dd>
<dt>
</dt><dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>keyword</i>=&quot;<i>value</i>&quot;</dd></dl>
<p> The <code>locale</code> command also knows about the following options:</p>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Display additional information for some command-line option and argument combinations.</dd>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd> Display a summary of command-line options and arguments and exit.</dd>
<dt><code>&#8211;usage</code></dt>
<dd> Display a short usage message and exit.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Display the program version and exit.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/lib/locale/locale-archive</i></dt>
<dd> Usual default locale archive location.</dd>
<dt><i>/usr/share/i18n/locales</i></dt>
<dd> Usual default path for locale definition files.</dd></dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>EXAMPLES</h2>
<p> $ <code>locale</code> LANG=en_US.UTF-8 LC_CTYPE=&quot;en_US.UTF-8&quot; LC_NUMERIC=&quot;en_US.UTF-8&quot; LC_TIME=&quot;en_US.UTF-8&quot; LC_COLLATE=&quot;en_US.UTF-8&quot; LC_MONETARY=&quot;en_US.UTF-8&quot; LC_MESSAGES=&quot;en_US.UTF-8&quot; LC_PAPER=&quot;en_US.UTF-8&quot; LC_NAME=&quot;en_US.UTF-8&quot; LC_ADDRESS=&quot;en_US.UTF-8&quot; LC_TELEPHONE=&quot;en_US.UTF-8&quot; LC_MEASUREMENT=&quot;en_US.UTF-8&quot; LC_IDENTIFICATION=&quot;en_US.UTF-8&quot; LC_ALL= </p>
<p> $ <code>locale date_fmt</code> %a %b %e %H:%M:%S %Z %Y </p>
<p> $ <code>locale -k date_fmt</code> date_fmt=&quot;%a %b %e %H:%M:%S %Z %Y&quot; </p>
<p> $ <code>locale -ck date_fmt</code> LC_TIME date_fmt=&quot;%a %b %e %H:%M:%S %Z %Y&quot; </p>
<p> $ <code>locale LC_TELEPHONE</code> +%c (%a) %l (%a) %l 11 1 UTF-8 </p>
<p> $ <code>locale -k LC_TELEPHONE</code> tel_int_fmt=&quot;+%c (%a) %l&quot; tel_dom_fmt=&quot;(%a) %l&quot; int_select=&quot;11&quot; int_prefix=&quot;1&quot; telephone-codeset=&quot;UTF-8&quot; </p>
<p> The following example compiles a custom locale from the <i>./wrk</i> directory with the <code><a href="/docs/linux/man/1-localedef/">localedef</a></code>(1) utility under the <i>$HOME/.locale</i> directory, then tests the result with the <code><a href="/docs/linux/man/1-date/">date</a></code>(1) command, and then sets the environment variables <code>LOCPATH</code> and <code>LANG</code> in the shell profile file so that the custom locale will be used in the subsequent user sessions: </p>
<p> $ <code>mkdir -p $HOME/.locale</code> $ <code>I18NPATH=./wrk/ localedef -f UTF-8 -i fi_SE $HOME/.locale/fi_SE.UTF-8</code> $ <code>LOCPATH=$HOME/.locale LC_ALL=fi_SE.UTF-8 date</code> $ <code>echo &quot;export LOCPATH=\$HOME/.locale&quot; &gt;&gt; $HOME/.bashrc</code> $ <code>echo &quot;export LANG=fi_SE.UTF-8&quot; &gt;&gt; $HOME/.bashrc</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-localedef/">localedef</a></code>(1), <code><a href="/docs/linux/man/5-charmap/">charmap</a></code>(5), <code><a href="/docs/linux/man/5-locale/">locale</a></code>(5), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
