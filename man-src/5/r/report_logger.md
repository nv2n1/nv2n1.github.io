---
title: "report_logger(5)"
name: "report_logger"
section: "5"
letter: "r"
url: "/docs/linux/man/5-report_logger/"
---

report_logger.conf - configuration file for libreport.

<h2>Description</h2>

This configuration file specifies which of the work flow definitions are applicable to analyzing problems and export the problem data information to a text file. 

 All applicable work flows are presented to users in User Interface as possibilities for processing of any problems. A particular work flow becomes applicable if its conditions are satisfied. 

 This configuration file consists from condition lines. Each condition line must start with EVENT=workflow_NAME where &quot;workflow_&quot; is constant prefix and &quot;workflow_NAME&quot; is base name of path to reporting work flow configuration file. 

 The rest of condition line has form VAR=VAL, VAR!=VAL or VAL~=REGEX, where VAR is a name of problem directory element to be checked (for example, &quot;executable&quot;, &quot;package&quot;, hostname&quot; etc). The condition may consists from as many element checks as it is necessary. 

 All condition lines in this configuration file are commented out by default. Therefore all applicable work flows from this file are not presented to users in User Interface. For enable this extension uncomment all condition line in this configuration file.

<h2>Examples</h2>

Condition line
<dl><dd>EVENT=workflow_LoggerCCpp analyzer=CCpp</dl>
 

 The condition line above expects existence of /usr/share/libreport/workflows/workflow_LoggerCCpp.xml

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-report-gtk/">report-gtk</a>(1)

<h2>Author</h2>

<dl><dd>&bull; ABRT team</dl>
