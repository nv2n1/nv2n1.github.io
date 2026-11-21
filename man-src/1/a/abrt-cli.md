---
title: "abrt-cli(1)"
name: "abrt-cli"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-cli/"
---

<h2 class="name">NAME</h2>
 

 abrt-cli - List, remove, print, analyze, report problems 

<h2>SYNOPSIS</h2>

 

 <i>abrt-cli</i> [--authenticate] COMMAND [COMMAND OPTIONS] 

 <i>abrt-cli</i> list [-vn] [--detailed] [--since NUM] [--until NUM] [DIR]... 

 <i>abrt-cli</i> remove [-v] DIR... 

 <i>abrt-cli</i> report [-v] [--delete] DIR... 

 <i>abrt-cli</i> info [-v] [--detailed] [-s SIZE] DIR... 

 <i>abrt-cli</i> status [-vb] [--since NUM] 

 <i>abrt-cli</i> process [-v] [--since NUM] DIR...

<h2>GLOBAL OPTIONS</h2>

 

 -a,--authenticate
<dl>
<dt>
</dt><dd> Enable PolicyKit authentication to be able to work with the system problems</dd></dl>

<h2>COMMAND OPTIONS</h2>

 

 -v,--verbose
<dl>
<dt>
</dt><dd> Be more verbose. Can be given multiple times.</dd></dl>
 

 -b, --bare
<dl>
<dt>
</dt><dd> Print only the problem count without any message</dd></dl>
 

 --detailed
<dl>
<dt>
</dt><dd> Show detailed report</dd></dl>
 

 --delete
<dl>
<dt>
</dt><dd> Remove PROBLEM_DIR after reporting</dd></dl>
 

 -n,--not-reported
<dl>
<dt>
</dt><dd> List only not-reported problems</dd></dl>
 

 --size SIZE
<dl>
<dt>
</dt><dd> Text larger than SIZE bytes will be shown abridged</dd></dl>
 

 --since NUM
<dl>
<dt>
</dt><dd> Selects only problems detected after timestamp</dd></dl>
 

 --until NUM
<dl>
<dt>
</dt><dd> Selects only the problems older than specified timestamp</dd></dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
</dt><dd> &bull; ABRT team</dd></dl>
