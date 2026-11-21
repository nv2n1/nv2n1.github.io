---

title: "abrt-action-analyze-core(1)"
name: "abrt-action-analyze-core"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-analyze-core/"
---

abrt-action-analyze-core - Extracts builds from a core dump 

<i>abrt-action-analyze-core</i> [-v] [-o OUTFILE] -c COREFILE

The tool reads a core dump and extracts build ids of loaded modules and prints the list to the standard output if the OUTFILE file is not configured.

<h2>OPTIONS</h2>

 

 -c COREFILE
<dl>
<dt>
</dt><dd> Path to a core dump.</dd></dl>
 

 -v
<dl>
<dt>
</dt><dd> Be more verbose. Can be given multiple times.</dd></dl>
 

 -o OUTFILE
<dl>
<dt>
</dt><dd> Output file</dd></dl>
 

 -h, --help
<dl>
<dt>
</dt><dd> Prints help text</dd></dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
</dt><dd> &bull; ABRT team</dd></dl>
