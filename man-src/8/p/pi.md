---
title: "pi(8)"
name: "pi"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pi/"
---

&nbsp;<wbr>-&nbsp;<wbr>

<h2>Synopsis</h2>

Print help about puppet types on the console. Run with aq-haq to get detailed help.

<h2>Usage</h2>

pi [-h|--help] [-s|--short] [-p|--providers] [-l|--list] [-m|--meta]

<h2>Description</h2>

Prints details of Puppet types, providers and metaparameters on the console.

<h2>Options</h2>

help: Print this help text 

 providers: Describe providers in detail for each type 

 list: List all types 

 meta: List all metaparameters 

 short: List only parameters without detail

<h2>Example</h2>

pi --list pi file --providers pi user -s -m

<h2>Author</h2>

David Lutterkort

<h2>Copyright</h2>

Copyright (c) 2005 Puppet Labs, LLC Licensed under the GNU Public License
