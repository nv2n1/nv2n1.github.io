---
title: "mrtglib(1)"
name: "mrtglib"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrtglib/"
---

<h2 class="name">NAME</h2>
 

 MRTG_lib.pm - Library for MRTG and support scripts 

<h2>SYNOPSIS</h2>

 <pre><code>
use MRTG_lib;
my($configfile, @target_names, % globalcfg, % targetcfg);
readcfg($configfile, \@target_names, \% globalcfg, \% targetcfg);
my(@parsed_targets);
cfgcheck(\@target_names, \% globalcfg, \% targetcfg, \@parsed_targets);
</code></pre>

<h2>DESCRIPTION</h2>

 MRTG_lib is part of <font SIZE="-1">MRTG</font>, the Multi Router Traffic Grapher. It was separated from <font SIZE="-1">MRTG</font> to allow other programs to easily use the same config files. The main part of MRTG_lib is the config file parser but some other funcions are there too.
<dl>
<dt>$MRTG_lib::OS
<dd> Type of <font SIZE="-1">OS:</font> <font SIZE="-1">WIN</font>, <font SIZE="-1">UNIX</font>, <font SIZE="-1">VMS</font>
<dt>$MRTG_lib::SL
<dd> <i>Slash</i> in the current <font SIZE="-1">OS</font>.
<dt>$MRTG_lib::PS
<dd> Path separator in <font SIZE="-1">PATH</font> variable
<dt>&quot;readcfg&quot;
<dd> <tt>&quot;readcfg($file, \@targets, \%globalcfg, \%targetcfg [, $prefix, \%extrules])&quot;</tt> 

 Reads a config file, parses it and fills some arrays and hashes. The mandatory arguments are: the name of the config file, a ref to an array which will be filled with a list of the target names, a hashref for the global configuration, a hashref for the target configuration. 

 The configuration file syntax is: 

 
globaloption : value
                   targetoption[targetname] : value
                                                  aprefix *extglobal : value
                                                                           aprefix *exttarget[target2] : value
 

 E.g. 

 
workdir : / var / stat / mrtg target[router1] : 2 : public[at] router1.local.net 14all * columns : 2
 

 The global config hash has the structure 

 <pre>
 $globalcfg{configoption} = 'value'
</pre> 

 The target config hash has the structure 

 
$targetcfg{configoption} {targetname} = 'value'
 

 See mrtg-reference for more information about the <font SIZE="-1">MRTG</font> configuration syntax. 

 <tt>&quot;readcfg&quot;</tt> can take two additional arguments to extend the config file syntax. This allows programs to put their configuration into the mrtg config file. The fifth argument is the prefix of the extension, the sixth argument is a hash with the checkrules for these extension settings. E.g. if the prefix is ``14all'' <tt>&quot;readcfg&quot;</tt> will check config lines that begin with ``14all*'', i.e. all lines like 

 <pre>
 14all*columns: 2
 14all*graphsize[target3]: 500 200
</pre> 

 against the rules in <tt>%extrules</tt>. The format of this hash is: 

 
$extrules{option} = [ sub{$_[0] = ~m / ^\d + $ / }, sub{"Error message for $_[0]"} ] i.e.$extrules{option}[0]-&gt;a test expression
                        $extrules{option}[1]
                            -&gt;error message if test fails
 

 The first part of the array is a perl expression to test the value of the option. The test can access this value in the variable ``$arg''. The second part of the array is an error message to display when the test fails. The failed value can be integrated by using the variable ``$arg''. 

 Config settings with an different prefix than the one given in the <tt>&quot;readcfg&quot;</tt> call are not checked but inserted into <i></i>%globalcfg<i></i> and <i></i>%targetcfg<i></i>. Prefixed settings keep their prefix in the config hashes: 

 
$targetcfg{'14all*graphsize'} {'target3'} = '500 200'

<dt>&quot;cfgcheck&quot;
<dd> <tt>&quot;cfgcheck(\@target_names, \%globalcfg, \%targetcfg, \@parsed_targets)&quot;</tt> 

 Checks the configuration read by <tt>&quot;readcfg&quot;</tt>. Checks the values in the config for syntactical and/or semantical errors. Sets defaults for some options. Parses the ``target[...]'' options and filles the array <tt>@parsed_targets</tt> ready for mrtg functions. 

 The first three arguments are the same as for <tt>&quot;readcfg&quot;</tt>. The fourth argument is an arrayref which will be filled with the parsed target defs. 

 <tt>&quot;cfgcheck&quot;</tt> converts the values of target settings <i>options</i>, e.g. 

 <pre>
 options[router1]: bits, growright
</pre> 

 to a hash: 

 
$targetcfg{'option'} {'bits'} {'router1'} = 1 $targetcfg{'option'} {'growright'} {'router1'} = 1
 

 This is not done by <tt>&quot;readcfg&quot;</tt> so if you don't use <tt>&quot;cfgcheck&quot;</tt> you have to check the scalar variable <i></i>$targetcfg<i>{'option'}{'router1'}</i> (<font SIZE="-1">MRTG</font> allows options to be separated by space or ',').
<dt>&quot;ensureSL&quot;
<dd> <tt>&quot;ensureSL(\$pathname)&quot;</tt> 

 Checks that the <i>pathname</i> does not contain double path separators and ends with a path separator. It uses <tt>$MRTG_lib::SL</tt> as path separator which will be / or \ depending on the <font SIZE="-1">OS</font>.
<dt>&quot;log2rrd&quot;
<dd> <tt>&quot;log2rrd ($router,\%globalcfg,\%targetcfg)&quot;</tt> 

 Convert log file to rrd format. Needs rrdtool.
<dt>&quot;datestr&quot;
<dd> <tt>&quot;datestr(time)&quot;</tt> 

 Returns the time given in the argument as a nicely formated date string. The argument has to be in <font SIZE="-1">UNIX</font> time format (seconds since 1970-1-1).
<dt>&quot;timestamp&quot;
<dd> <tt>&quot;timestamp()&quot;</tt> 

 Return a string representing the current time.
<dt>&quot;setup_loghandlers&quot;
<dd> <tt>&quot;setup_loghandlers(filename)&quot;</tt> 

 Install signalhandlers for __DIE__ and __WARN__ making the errors go the the specified destination. If filename is 'eventlog' mrtg will log to the windows event logger.
<dt>&quot;expistr&quot;
<dd> <tt>&quot;expistr(time)&quot;</tt> 

 Returns the time given in the argument formatted suitable for <font SIZE="-1">HTTP</font> Expire-Headers.
<dt>&quot;create_pid&quot;
<dd> <tt>&quot;create_pid()&quot;</tt> 

 Creates a pid file for the mrtg daemon
<dt>&quot;demonize_me&quot;
<dd> <tt>&quot;demonize_me()&quot;</tt> 

 Puts the running program into background, detaching it from the terminal.
<dt>&quot;populatecache&quot;
<dd> <tt>&quot;populatecache(\%confcache, $host, $reread, $snmpoptshash)&quot;</tt> 

 Reads the <font SIZE="-1">SNMP</font> variables <i>ifDescr</i>, <i>ipAdEntIfIndex</i>, <i>ifPhysAddress</i>, <i>ifName</i> from the <i>host</i> and stores the values in <i></i>%confcache<i></i> as follows: 

 <pre><code>
$confcache{$host} {'Descr'} {ifDescr} {oid} = (ifDescr or 'Dup')
    $confcache{$host} {'IP'} {ipAdEntIfIndex} {oid} = (ipAdEntIfIndex or 'Dup')
        $confcache{$host} {'Eth'} {ifPhysAddress} {oid} = (ifPhysAddress or 'Dup')
            $confcache{$host} {'Name'} {ifName} {oid} = (ifName or 'Dup')
                $confcache{$host} {'Type'} {ifType} {oid} = (ifType or 'Dup')
</code></pre> 

 The value (at the right side of =) is 'Dup' if a value was retrieved muliple times, the retrieved value else.
<dt>&quot;readconfcache&quot;
<dd> <tt>&quot;my $confcache = readconfcache($file)&quot;</tt> 

 Preload the confcache from a file.
<dt>&quot;readfromconfcache&quot;
<dd> <tt>&quot;writeconfcache($confcache,$file)&quot;</tt> 

 Store the current confcache into a file.
<dt>&quot;writeconfcache&quot;
<dd> <tt>&quot;writeconfcache($confcache,$file)&quot;</tt> 

 Store the current confcache into a file.
<dt>&quot;storeincache&quot;
<dd> <tt>&quot;storeincache($confcache,$host,$method,$key,$value)&quot;</tt>
<dt>&quot;readfromcache&quot;
<dd> <tt>&quot;readfromcache($confcache,$host,$method,$key)&quot;</tt>
<dt>&quot;clearfromcache&quot;
<dd> <tt>&quot;clearfromcache($confcache,$host)&quot;</tt>
<dt>&quot;debug&quot;
<dd> <tt>&quot;debug($type, $message)&quot;</tt> 

 Prints the <i>message</i> on <font SIZE="-1">STDERR</font> if debugging is enabled for type <i>type</i>. A debug type is enabled if <i>type</i> is in array <tt>@main::DEBUG</tt>.</dl>

<h2>AUTHORS</h2>

 Rainer Bawidamann &lt;Rainer.Bawidamann [at] rz.uni-ulm.de&gt; 

 (This Manpage) 

<h2>Index</h2>


