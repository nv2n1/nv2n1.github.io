---

title: "func-transmit(1)"
name: "func-transmit"
section: "1"
letter: "f"
url: "/docs/linux/man/1-func-transmit/"
---

Func-transmit -- cross-language func adapter

<h2>SYNOPSIS</h2>

 func-transmit [-h|--help] [-j|--json] [-y|--yaml] &lt; data_in &gt; data_out

<h2>DESCRIPTION</h2>

 Func includes a powerful Python API for addressing the overlord via software. When writing an app in a language other than Python, func-transmit can be used to operate the overlord and recieve structured results from it. 

 This tool, func-transmit, is intended to be called using pipes, sending formatted data into stdin and recieving return codes via stdout. It also can be invoked using the shell.

<h2>FORMATS AND USAGE</h2>

 The input and output format is either JSON or YAML 1.0. The default is JSON. The [--yaml] option enables YAML support. 

 The data formats used by Func transmit are described in more detail (with examples) at <a rel="nofollow" HREF="https://fedorahosted.org/func/wiki/FuncTransmit">https://fedorahosted.org/func/wiki/FuncTransmit</a>

<h2>EXIT_STATUS</h2>

 Generally func-transmit should always return 0 if loading is successful. Return data is then expressed in the output stream, to be interpreted by a JSON or YAML module at the other end of the pipe. Non-zero return codes indicate more serious setup problems. 

 Func-transmit will exit after every command issued to the overlord, it does not await further input on the pipes.

<h2>ADDITONAL RESOURCES</h2>

 See <a rel="nofollow" HREF="https://fedorahosted.org/func/">https://fedorahosted.org/func/</a> for more information. 

 See also the manpages for ``func-inventory'', ``funcd'', ``certmaster'', and ``certmaster-ca''.

<h2>AUTHOR</h2>

 Various. See <a rel="nofollow" HREF="https://fedorahosted.org/func/">https://fedorahosted.org/func/</a>
