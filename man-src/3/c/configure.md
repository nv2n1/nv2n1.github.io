---
title: "configure(3)"
name: "configure"
section: "3"
letter: "c"
url: "/docs/linux/man/3-configure/"
---

XMLTV::Configure - Configuration file handling for XMLTV grabbers 

<h2>Description</h2>Utility library that helps grabbers read from configuration files and implement a configuration method that can be run from the command-line.
<h2>Exported Functions</h2>All these functions are exported on demand.
<dl COMPACT><dt>LoadConfig
<dd>Takes the name of the configuration file to load as a parameter. 

 Returns a hashref with configuration fieldnames as keys. Note that the values of the hash are references to an array of values. 

 Example: 
&nbsp;<wbr>&nbsp;<wbr>{ 
&nbsp;<wbr>username&nbsp;<wbr>=&gt;&nbsp;<wbr>[&nbsp;<wbr>'mattias'&nbsp;<wbr>], 
&nbsp;<wbr>password&nbsp;<wbr>=&gt;&nbsp;<wbr>[&nbsp;<wbr>'xxx'&nbsp;<wbr>], 
&nbsp;<wbr>channel&nbsp;<wbr>=&gt;&nbsp;<wbr>[&nbsp;<wbr>'svt1.svt.se',&nbsp;<wbr>'kanal5.se'&nbsp;<wbr>], 
&nbsp;<wbr>no_channel&nbsp;<wbr>=&gt;&nbsp;<wbr>['svt2.svt.se'&nbsp;<wbr>], 
&nbsp;<wbr>&nbsp;<wbr>} 

 Note that unselected options from a selectmany are collected in an entry named after the key with a prefix of 'no_'. See the channel and no_channel entry in the example. They are the result of a selectmany with id=channel. 

 The configuration file must be in the format described in the file ``ConfigurationFiles.txt''. If the file does not exist or if the format is wrong, LoadConfig returns undef.
<dt>SaveConfig
<dd>Write a configuration hash in the format returned by LoadConfig to a file that can be loaded with LoadConfig. Takes two parameters, a reference to a configuration hash and a filename. 

 Note that a grabber should normally never have to call SaveConfig. This is done by the Configure-method.
<dt>Configure
<dd>Generates a configuration file for the grabber. 

 Takes three parameters: stagesub, listsub and the name of the configuration file. 

 stagesub shall be a coderef that takes a stage-name or undef and a configuration hashref as a parameter and returns an xml-string that describes the configuration necessary for that stage. The xml-string shall follow the xmltv-configuration.dtd. 

 listsub shall be a coderef that takes a configuration hash as returned by LoadConfig as the first parameter and an option hash as returned by ParseOptions as the second parameter and returns an xml-string containing a list of all the channels that the grabber can deliver data for using the supplied configuration. Note that the listsub shall not use any channel-configuration from the hashref.</dl><h2>Copyright</h2>Copyright (C) 2005 Mattias Holmlund. 

 This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301, USA.</font>
