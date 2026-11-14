---
title: "functions(1)"
name: "functions"
section: "1"
letter: "f"
url: "/docs/linux/man/1-functions/"
---

<h2 class="name">NAME</h2>
 

 functions - print or erase functions

<h3>Synopsis</h3>

 functions [-e] FUNCTIONS...

<h3>Description</h3>

 This builtin command is used to print or erase functions. 

<dl>
<dt>*
<dd> -a or --all list all functions, even those whose name start with an underscore.
<dt>*
<dd> -d DESCRIPTION or --description=DESCRIPTION change the description of this function
<dt>*
<dd> -e or --erase causes the specified functions to be erased.
<dt>*
<dd> -h or --help display a help message and exit
<dt>*
<dd> -n or --names list only the names of all defined functions, not their definition
<dt>*
<dd> -q or --query test if the specified functions exist. Does not output anything, but the builtins exit status is the number of functions specified that were not defined.</dl>
 

 

 The default behavior of functions when called with no arguments, is to print the names and definitions of all defined functions. If any non-switch parameters are given, only the definition of the specified functions are printed. 

 Automatically loaded functions can not be removed using functions -e. Either remove the definition file or change the $fish_function_path variable to remove autoloaded functions. 

 The exit status of the functions builtin is the number functions specified in the argument list that do not exist. 

<h2>Index</h2>


