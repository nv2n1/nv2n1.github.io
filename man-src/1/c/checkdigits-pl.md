---
title: "checkdigits-pl(1)"
name: "checkdigits-pl"
section: "1"
letter: "c"
url: "/docs/linux/man/1-checkdigits-pl/"
---

checkdigits - check or generate check digits 

<h2>Version</h2>This document describes checkdigits v1.3.2
<h2>Synopsis</h2><pre> checkdigits [Options] command [[number] ...]
 options:
 -algorithm alg - use this algorithm
 commands:
 check - check validity of number containing checkdigit
 checkdigit - return checkdigit belonging to number
 complete - return number completed with checkdigit
 list_algorithms - list all known algorithms
 describe - describe the given algorithms</pre><h2>Description</h2>This is a command line program that may be used to compute any checkdigit known by the perl module Algorithm::CheckDigits.
<h2>Options And Commands</h2><h3>Options</h3><i>-algorithm alg</i> 

 Compute checkdigits according to algorithm <i>alg</i>. Instead of providing the algorithm with this option, you may choose to rename the program to the name of the algorithm or to <tt>&quot;checkdigits-&quot;</tt> followed by the name of the algorithm. 

 You must provide the algorithm with any of these means or the program will not compute any checkdigit.
<h3>Commands</h3><i>check</i> 

 <i>checkdigit</i> 

 <i>complete</i> 

 When called with this command, the program will take the number compute the appropriate checkdigits and return the complete number with checkdigits. 

 <i>describe</i> 

 Called with this command, the program will list the algorithm handles given on the command line with a short description or the word ``unknown'' for any unknown algorithm. See command <i>list_algorithms</i> for a list of known algorithms. 

 <i>list_algorithms</i> 

 Called with this command, the program will list all known algorithms together with a short description and then exit.
<h2>Diagnostics</h2><h2>Configuration And Environment</h2>At the moment the program doesn't recognise any environment variables. 

 The algorithm to use may be predefined by renaming the program to the name of the algorithm or to <tt>&quot;checkdigits-&quot;</tt> followed by the name of the algorithm.
<h2>Author</h2>Mathias Weidner <tt>&quot;mamawe [at] cpan.org&quot;</tt>
<h2>Licence And Copyright</h2>Copyright (c) 2010, Mathias Weidner <tt>&quot;mamawe [at] cpan.org&quot;</tt>. All rights reserved. 

 This module is free software; you can redistribute it and/or modify it under the same terms as Perl itself. See perlartistic.
<h2>Disclaimer Of Warranty</h2><font SIZE="-1">BECAUSE THIS SOFTWARE IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY FOR THE SOFTWARE, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE SOFTWARE ``AS IS'' WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE SOFTWARE IS WITH YOU. SHOULD THE SOFTWARE PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR, OR CORRECTION.</font> 

 <font SIZE="-1">IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR REDISTRIBUTE THE SOFTWARE AS PERMITTED BY THE ABOVE LICENCE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE SOFTWARE </font>(<font SIZE="-1">INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE SOFTWARE TO OPERATE WITH ANY OTHER SOFTWARE</font>), <font SIZE="-1">EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.</font>
