---
title: "report-gtk(1)"
name: "report-gtk"
section: "1"
letter: "r"
url: "/docs/linux/man/1-report-gtk/"
---

<h2 class="name">NAME</h2>
 

 report-gtk - GUI tool to analyze and report ABRT problems 

<h2>SYNOPSIS</h2>

 

 <i>report-gtk</i> [-vpdx] [-e EVENT] [-g GUI_FILE] PROBLEM_DIR

<h2>DESCRIPTION</h2>

 

 <i>report-gtk</i> is a graphical tool that reports application crashes and other problems caught by abrtd daemon, or created by other programs using libreport. report-gtk works with a single problem saved in specified PROBLEM_DIR. In the expert mode it enables access to and manipulation of problem data.

<h2>OPTIONS</h2>

 

 -d, --delete
<dl>
<dt>
<dd> Remove PROBLEM_DIR after reporting</dl>
 

 -e EVENT
<dl>
<dt>
<dd> Run only theset EVENTs on PROBLEM_DIR</dl>
 

 -g FILE
<dl>
<dt>
<dd> Alternate GUI file</dl>
 

 -p
<dl>
<dt>
<dd> Add program names to log</dl>
 

 -v, --verbose
<dl>
<dt>
<dd> Be verbose</dl>
 

 -V, --version
<dl>
<dt>
<dd> Display version and exit</dl>
 

 -x, --expert
<dl>
<dt>
<dd> Enabled advanced features</dl>

<h2>CONFIGURATION</h2>

<h3>Reporting work flow configuration</h3>

 

 These configuration files are placed in /usr/share/libreport/workflows. 

 Each file has XML formatting with the following DTD: 

<dl>
<dt>
<dd> <pre>
&lt;!ELEMENT workflow    (name+,description+,events*)&gt;
&lt;!ELEMENT name        (#PCDATA)&gt;
&lt;!ATTLIST name         xml:lang CDATA #IMPLIED&gt;
&lt;!ELEMENT description (#PCDATA)&gt;
&lt;!ATTLIST description  xml:lang CDATA #IMPLIED&gt;
&lt;!ELEMENT events =    (event)+&gt;
&lt;!ELEMENT event =     (#PCDATA)&gt;
</pre></dl>
 

 name
<dl>
<dt>
<dd> User visible name</dl>
 

 description
<dl>
<dt>
<dd> User visible description</dl>
 

 events
<dl>
<dt>
<dd> List of executed events</dl>
 

 event
<dl>
<dt>
<dd> Name of event. If event is not applicable on the problem data or if it is not defined then process continues with next event sibling.</dl>

<h2>EXAMPLES</h2>

<h3>Simple reporting work flow</h3>

 

<dl>
<dt>
<dd> <pre>
&lt;workflow&gt;
  &lt;name xml:lang=&quot;en&quot;&gt;Example&lt;/name&gt;
  &lt;name xml:lang=&quot;cs&quot;&gt;Př&iacute;klad&lt;/name&gt;
  &lt;description xml:lang=&quot;en&quot;&gt;Example description&lt;/description&gt;
  &lt;description xml:lang=&quot;cs&quot;&gt;Př&iacute;klad popisu&lt;/description&gt;
  &lt;evetns&gt;
     &lt;event&gt;analyze_example&lt;/event&gt;
     &lt;event&gt;collect_example&lt;/event&gt;
     &lt;event&gt;report_example&lt;/event&gt;
  &lt;/events&gt;
&lt;/workflow&gt;
</pre></dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


