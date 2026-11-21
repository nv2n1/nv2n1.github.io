---

title: "abrt-action-analyze-c(1)"
name: "abrt-action-analyze-c"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-analyze-c/"
---

abrt-action-analyze-c - Calculate and save UUID for a problem data directory DIR with coredump. 

<i>abrt-action-analyze-c</i> [-v] [-d DIR]

The tool reads the file named <i>coredump</i> from a problem data directory, processes it and generates a universally unique identifier (UUID). Then it saves this data as new element <i>uuid</i>.

<h3>Integration with ABRT events</h3>

 

 <i>abrt-action-analyze-c</i> can be used to generate the UUID of a newly saved coredump. 

<dl>
<dt>
</dt><dd> <pre>
EVENT=post-create analyzer=CCpp   abrt-action-analyze-c
</pre></dd></dl>

<h2>OPTIONS</h2>

 

 -d DIR
<dl>
<dt>
</dt><dd> Path to a problem directory. Current working directory is used when this option is not provided.</dd></dl>
 

 -v
<dl>
<dt>
</dt><dd> Be more verbose. Can be given multiple times.</dd></dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
</dt><dd> &bull; ABRT team</dd></dl>
