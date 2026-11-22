---

title: "tv_find_grabbers(1)"
name: "tv_find_grabbers"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_find_grabbers/"
---

tv_find_grabbers - Find all XMLTV grabbers that are installed on the system. 

<h2>SYNOPSIS</h2>

 tv_find_grabbers --help 

 tv_find_grabbers [-I &lt;dir&gt;] [--slow] [capability] ...

<h2>DESCRIPTION</h2>

 tv_find_grabbers searches the PATH for XMLTV grabbers and returns a list of all grabbers that it finds. The list contains one entry per line in the format 

 /usr/bin/tv_grab_fr|France 

 i.e. the name of the executable and the region that it serves, separated by a vertical bar.

<h2>OPTIONS</h2>

 -I &lt;dir&gt; Include a directory in the search for grabbers. May be used 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>multiple times. The default is to search the&nbsp;<wbr>PATH. 

 --slow When checking grabbers, compile and run them instead of searching 
&nbsp;<wbr>their source code for capabilities and description 

 --verbose Print progress information to STDERR.

<h2>AUTHOR</h2>

 Mattias Holmlund, mattias -at- holmlund -dot- se.

<h2>COPYRIGHT</h2>

 Copyright (C) 2005 Mattias Holmlund. 

 This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. 

 You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
