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
<dd> Enable PolicyKit authentication to be able to work with the system problems</dl>

<h2>COMMAND OPTIONS</h2>

 

 -v,--verbose
<dl>
<dt>
<dd> Be more verbose. Can be given multiple times.</dl>
 

 -b, --bare
<dl>
<dt>
<dd> Print only the problem count without any message</dl>
 

 --detailed
<dl>
<dt>
<dd> Show detailed report</dl>
 

 --delete
<dl>
<dt>
<dd> Remove PROBLEM_DIR after reporting</dl>
 

 -n,--not-reported
<dl>
<dt>
<dd> List only not-reported problems</dl>
 

 --size SIZE
<dl>
<dt>
<dd> Text larger than SIZE bytes will be shown abridged</dl>
 

 --since NUM
<dl>
<dt>
<dd> Selects only problems detected after timestamp</dl>
 

 --until NUM
<dl>
<dt>
<dd> Selects only the problems older than specified timestamp</dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


