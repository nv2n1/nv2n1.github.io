---

title: "mateconf-gsettings-schema-convert(1)"
name: "mateconf-gsettings-schema-convert"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mateconf-gsettings-schema-convert/"
description: "mateconf-gsettings-schema-convert – MateConf to GSettings schema conversion"
---

<dl>
<dt> <code>mateconf-gsettings-schema-convert</code> [option&#8230;] {file}</dt></dl>
<p> <code>mateconf-gsettings-schema-convert</code></p>
<dd>converts between MateConf and GSettings schema file formats. Note that the conversion is not expected to be fully automated. You are expected to verify and edit the result of the conversion. </dd>
<p> Note that GSettings schemas need to be converted into binary form with glib-compile-schemas before they can be used by applications.</p>
<h3>Options</h3>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Print help and exit</dd></dl>
<p> <code>-o </code><i>OUTPUT</i>, <code>&#8211;output=</code><i>OUTPUT</i></p>
<dl>
<dt>
</dt><dd> Store the generated output in the file <i>OUTPUT</i>. If no output file is specified, the generated output is written to stdout.</dd></dl>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dt>
</dt><dd> Overwrite the output file if it already exists.</dd></dl>
<p> <code>-g</code>, <code>&#8211;mateconf</code></p>
<dl>
<dt>
</dt><dd> The input file is a MateConf schema.</dd></dl>
<p> <code>-s</code>, <code>&#8211;simple</code></p>
<dl>
<dt>
</dt><dd> Produce a GSettings schema in simple format. The simple format is easier to edit and can be converted into the XML format with <code>mateconf-gsettings-schema-convert</code> later on.</dd></dl>
<p> <code>-x</code>, <code>&#8211;xml</code></p>
<dl>
<dt>
</dt><dd> Produce a GSettings schema in XML format. If the output format is not explicitly specified, this is the default.</dd></dl>
<p> <code>-i </code><i>ID</i>, <code>&#8211;schema-id=</code><i>ID</i></p>
<dl>
<dt>
</dt><dd> Use <i>ID</i> as the schema id in the generated GSettings schema.</dd></dl>
<p> <code>-d </code><i>DOMAIN</i>, <code>&#8211;gettext-domain=</code><i>DOMAIN</i></p>
<dl>
<dt>
</dt><dd> Use <i>DOMAIN</i> as the gettext domain in the generated GSettings schema.</dd></dl>
<p> <code>-u</code>, <code>&#8211;keep-underscores</code></p>
<dl>
<dt>
</dt><dd> Keep underscores in key names instead of replacing them with dashes. GSettings keys should not contain any underscore.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mateconf-gsettings-data-convert/">mateconf-gsettings-data-convert</a></code>(1) a related command to migrate user settings from MateConf to GSettings. </p>
