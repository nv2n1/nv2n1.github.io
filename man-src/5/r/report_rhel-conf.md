---
title: "report_rhel-conf(5)"
name: "report_rhel-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-report_rhel-conf/"
---

report_rhel.conf - configuration file for libreport.

<h2>Description</h2>

This configuration file specifies which of the reporting work flow definitions are applicable for all problems types on Red Hat Enterprise Linux. 

 All applicable reporting work flows are presented to users in User Interface as possibilities for processing of particular problem in <i>anaconda</i> package. 

 This configuration file consists from one condition per line. 

 Each condition line must start with EVENT=workflow_NAME where &quot;workflow_&quot; is constant prefix and &quot;workflow_NAME&quot; is base name of path to reporting work flow configuration file. 

 The rest of condition line has form VAR=VAL, VAR!=VAL or VAL~=REGEX, where VAR is a name of problem directory element to be checked (for example, &quot;executable&quot;, &quot;package&quot;, hostname&quot; etc). The condition may consists from as many element checks as it is necessary.

<h2>Examples</h2>

Condition line
<dl><dd>EVENT=workflow_RHELCCpp analyzer=CCpp</dl>
 

 The condition line above expects existence of /usr/share/libreport/workflows/workflow_RHELCCpp.xml

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-report-gtk/">report-gtk</a>(1)

<h2>Author</h2>

<dl><dd>&bull; ABRT team</dl>
