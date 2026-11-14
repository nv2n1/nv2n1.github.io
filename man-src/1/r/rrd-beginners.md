---
title: "rrd-beginners(1)"
name: "rrd-beginners"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrd-beginners/"
description: "rrd-beginners – RRDtool Beginners’ Guide"
---

<h2 class="name">NAME</h2>
<p> rrd-beginners &#8211; RRDtool Beginners&#8217; Guide </p>
<h2>SYNOPSIS</h2>
<p> Helping new RRDtool users to understand the basics of RRDtool</p>
<h2>DESCRIPTION</h2>
<p> This manual is an attempt to assist beginners in understanding the concepts of RRDtool. It sheds a light on differences between RRDtool and other databases. With help of an example, it explains the structure of RRDtool database. This is followed by an overview of the &#8220;graph&#8221; feature of RRDtool. At the end, it has sample scripts that illustrate the usage/wrapping of RRDtool within Shell or Perl scripts.</p>
<h3>What makes RRDtool so special?</h3>
<p> RRDtool is <font SIZE="-1">GNU</font> licensed software developed by Tobias Oetiker, a system manager at the Swiss Federal Institute of Technology. Though it is a database, there are distinct differences between RRDtool databases and other databases as listed below:</p>
<dl>
<dt>&bull;</p>
<dd> RRDtool stores data; that makes it a back-end tool. The RRDtool command set allows the creation of graphs; that makes it a front-end tool as well. Other databases just store data and can not create graphs.</p>
<dt>&bull;</p>
<dd> In case of linear databases, new data gets appended at the bottom of the database table. Thus its size keeps on increasing, whereas the size of an RRDtool database is determined at creation time. Imagine an RRDtool database as the perimeter of a circle. Data is added along the perimeter. When new data reaches the starting point, it overwrites existing data. This way, the size of an RRDtool database always remains constant. The name &#8220;Round Robin&#8221; stems from this behavior.</p>
<dt>&bull;</p>
<dd> Other databases store the values as supplied. RRDtool can be configured to calculate the rate of change from the previous to the current value and store this information instead.</p>
<dt>&bull;</p>
<dd> Other databases get updated when values are supplied. The RRDtool database is structured in such a way that it needs data at predefined time intervals. If it does not get a new value during the interval, it stores an <font SIZE="-1">UNKNOWN</font> value for that interval. So, when using the RRDtool database, it is imperative to use scripts that run at regular intervals to ensure a constant data flow to update the RRDtool database.</dl>
<p> RRDtool is designed to store time series of data. With every data update, an associated time stamp is stored. Time is always expressed in seconds passed since epoch (01-01-1970). RRDtool can be installed on Unix as well as Windows. It comes with a command set to carry out various operations on <font SIZE="-1">RRD</font> databases. This command set can be accessed from the command line, as well as from Shell or Perl scripts. The scripts act as wrappers for accessing data stored in RRDtool databases.</p>
<h3>Understanding by an example</h3>
<p> The structure of an <font SIZE="-1">RRD</font> database is different than other linear databases. Other databases define tables with columns, and many other parameters. These definitions sometimes are very complex, especially in large databases. RRDtool databases are primarily used for monitoring purposes and hence are very simple in structure. The parameters that need to be defined are variables that hold values and archives of those values. Being time sensitive, a couple of time related parameters are also defined. Because of its structure, the definition of an RRDtool database also includes a provision to specify specific actions to take in the absence of update values. Data Source (<font SIZE="-1">DS</font>), heartbeat, Date Source Type (<font SIZE="-1">DST</font>), Round Robin Archive (<font SIZE="-1">RRA</font>), and Consolidation Function (<font SIZE="-1">CF</font>) are some of the terminologies related to RRDtool databases. </p>
<p> The structure of a database and the terminology associated with it can be best explained with an example. </p>
<pre>
 rrdtool create target.rrd \
         --start 1023654125 \
         --step 300 \
         DS:mem:GAUGE:600:0:671744 \
         RRA:AVERAGE:0.5:12:24 \
         RRA:AVERAGE:0.5:288:31
</pre>
<p> This example creates a database named <i>target.rrd</i>. Start time (1&#8217;023&#8217;654&#8217;125) is specified in total number of seconds since epoch (time in seconds since 01-01-1970). While updating the database, the update time is also specified. This update time <font SIZE="-1">MUST</font> be large (later) then start time and <font SIZE="-1">MUST</font> be in seconds since epoch. </p>
<p> The step of 300 seconds indicates that database expects new values every 300 seconds. The wrapper script should be scheduled to run every <code>step</code> seconds so that it updates the database every <code>step</code> seconds. </p>
<p> <font SIZE="-1">DS</font> (Data Source) is the actual variable which relates to the parameter on the device that is monitored. Its syntax is </p>
<pre>
 DS:variable_name:DST:heartbeat:min:max
</pre>
<p> <font SIZE="-1"><code>DS</code></font> is a key word. <tt>&quot;variable_name&quot;</tt> is a name under which the parameter is saved in the database. There can be as many DSs in a database as needed. After every step interval, a new value of <font SIZE="-1">DS</font> is supplied to update the database. This value is also called Primary Data Point <code>(</code><font SIZE="-1"><code>PDP</code></font><code>)</code>. In our example mentioned above, a new <font SIZE="-1">PDP</font> is generated every 300 seconds. </p>
<p> Note, that if you do <font SIZE="-1">NOT</font> supply new data points exactly every 300 seconds, this is not a problem, RRDtool will interpolate the data accordingly. </p>
<p> <font SIZE="-1"><code>DST</code></font> (Data Source Type) defines the type of the <font SIZE="-1">DS</font>. It can be <font SIZE="-1">COUNTER</font>, <font SIZE="-1">DERIVE</font>, <font SIZE="-1">ABSOLUTE</font>, <font SIZE="-1">GAUGE</font>. A <font SIZE="-1">DS</font> declared as <font SIZE="-1">COUNTER</font> will save the rate of change of the value over a step period. This assumes that the value is always increasing (the difference between the current and the previous value is greater than 0). Traffic counters on a router are an ideal candidate for using <font SIZE="-1">COUNTER</font> as <font SIZE="-1">DST</font>. <font SIZE="-1">DERIVE</font> is the same as <font SIZE="-1">COUNTER</font>, but it allows negative values as well. If you want to see the rate of <i>change</i> in free disk space on your server, then you might want to use the <font SIZE="-1">DERIVE</font> data type. <font SIZE="-1">ABSOLUTE</font> also saves the rate of change, but it assumes that the previous value is set to 0. The difference between the current and the previous value is always equal to the current value. Thus it just stores the current value divided by the step interval (300 seconds in our example). <font SIZE="-1">GAUGE</font> does not save the rate of change. It saves the actual value itself. There are no divisions or calculations. Memory consumption in a server is a typical example of gauge. The difference between the different types DSTs can be explained better with the following example: </p>
<pre>
 Values       = 300, 600, 900, 1200
 Step         = 300 seconds
 COUNTER DS   =    1,  1,   1,    1
 DERIVE DS    =    1,  1,   1,    1
 ABSOLUTE DS  =    1,  2,   3,    4
 GAUGE DS     = 300, 600, 900, 1200
</pre>
<p> The next parameter is <code>heartbeat</code>. In our example, heartbeat is 600 seconds. If the database does not get a new <font SIZE="-1">PDP</font> within 300 seconds, it will wait for another 300 seconds (total 600 seconds). If it doesn&#8217;t receive any <font SIZE="-1">PDP</font> within 600 seconds, it will save an <font SIZE="-1">UNKNOWN</font> value into the database. This <font SIZE="-1">UNKNOWN</font> value is a special feature of RRDtool &#8211; it is much better than to assume a missing value was 0 (zero) or any other number which might also be a valid data value. For example, the traffic flow counter on a router keeps increasing. Lets say, a value is missed for an interval and 0 is stored instead of <font SIZE="-1">UNKNOWN</font>. Now when the next value becomes available, it will calculate the difference between the current value and the previous value (0) which is not correct. So, inserting the value <font SIZE="-1">UNKNOWN</font> makes much more sense here. </p>
<p> The next two parameters are the minimum and maximum value, respectively. If the variable to be stored has predictable maximum and minimum values, this should be specified here. Any update value falling out of this range will be stored as <font SIZE="-1">UNKNOWN</font>. </p>
<p> The next line declares a round robin archive (<font SIZE="-1">RRA</font>). The syntax for declaring an <font SIZE="-1">RRA</font> is </p>
<pre>
 RRA:CF:xff:step:rows
</pre>
<p> <font SIZE="-1">RRA</font> is the keyword to declare RRAs. The consolidation function (<font SIZE="-1">CF</font>) can be <font SIZE="-1">AVERAGE</font>, <font SIZE="-1">MINIMUM</font>, <font SIZE="-1">MAXIMUM</font>, and <font SIZE="-1">LAST</font>. The concept of the consolidated data point (<font SIZE="-1">CDP</font>) comes into the picture here. A <font SIZE="-1">CDP</font> is CFed (averaged, maximum/minimum value or last value) from <i>step</i> number of PDPs. This <font SIZE="-1">RRA</font> will hold <i>rows</i> CDPs. </p>
<p> Lets have a look at the example above. For the first <font SIZE="-1">RRA</font>, 12 (steps) PDPs (<font SIZE="-1">DS</font> variables) are AVERAGEed (<font SIZE="-1">CF</font>) to form one <font SIZE="-1">CDP</font>. 24 (rows) of theses CDPs are archived. Each <font SIZE="-1">PDP</font> occurs at 300 seconds. 12 PDPs represent 12 times 300 seconds which is 1 hour. It means 1 <font SIZE="-1">CDP</font> (which is equal to 12 PDPs) represents data worth 1 hour. 24 such CDPs represent 1 day (1 hour times 24 CDPs). This means, this <font SIZE="-1">RRA</font> is an archive for one day. After 24 CDPs, <font SIZE="-1">CDP</font> number 25 will replace the 1st <font SIZE="-1">CDP</font>. The second <font SIZE="-1">RRA</font> saves 31 CDPs; each <font SIZE="-1">CPD</font> represents an <font SIZE="-1">AVERAGE</font> value for a day (288 PDPs, each covering 300 seconds = 24 hours). Therefore this <font SIZE="-1">RRA</font> is an archive for one month. A single database can have many RRAs. If there are multiple DSs, each individual <font SIZE="-1">RRA</font> will save data for all the DSs in the database. For example, if a database has 3 DSs and daily, weekly, monthly, and yearly RRAs are declared, then each <font SIZE="-1">RRA</font> will hold data from all 3 data sources.</p>
<h3>Graphical Magic</h3>
<p> Another important feature of RRDtool is its ability to create graphs. The &#8220;graph&#8221; command uses the &#8220;fetch&#8221; command internally to retrieve values from the database. With the retrieved values it draws graphs as defined by the parameters supplied on the command line. A single graph can show different <font SIZE="-1">DS</font> (Data Sources) from a database. It is also possible to show the values from more than one database in a single graph. Often, it is necessary to perform some math on the values retrieved from the database before plotting them. For example, in <font SIZE="-1">SNMP</font> replies, memory consumption values are usually specified in KBytes and traffic flow on interfaces is specified in Bytes. Graphs for these values will be more meaningful if values are represented in MBytes and mbps. The RRDtool graph command allows to define such conversions. Apart from mathematical calculations, it is also possible to perform logical operations such as greater than, less than, and if/then/else. If a database contains more than one <font SIZE="-1">RRA</font> archive, then a question may arise &#8211; how does RRDtool decide which <font SIZE="-1">RRA</font> archive to use for retrieving the values? RRDtool looks at several things when making its choice. First it makes sure that the <font SIZE="-1">RRA</font> covers as much of the graphing time frame as possible. Second it looks at the resolution of the <font SIZE="-1">RRA</font> compared to the resolution of the graph. It tries to find one which has the same or higher better resolution. With the &#8220;-r&#8221; option you can force RRDtool to assume a different resolution than the one calculated from the pixel width of the graph. </p>
<p> Values of different variables can be presented in 5 different shapes in a graph &#8211; <font SIZE="-1">AREA</font>, <font SIZE="-1">LINE1</font>, <font SIZE="-1">LINE2</font>, <font SIZE="-1">LINE3</font>, and <font SIZE="-1">STACK</font>. <font SIZE="-1">AREA</font> is represented by a solid colored area with values as the boundary of this area. <font SIZE="-1">LINE1/2/3</font> (increasing width) are just plain lines representing the values. <font SIZE="-1">STACK</font> is also an area but it is &#8220;stack&#8221;ed on top <font SIZE="-1">AREA</font> or <font SIZE="-1">LINE1/2/3</font>. Another important thing to note is that variables are plotted in the order they are defined in the graph command. Therefore care must be taken to define <font SIZE="-1">STACK</font> only after defining <font SIZE="-1">AREA/LINE</font>. It is also possible to put formatted comments within the graph. Detailed instructions can be found in the graph manual.</p>
<h3>Wrapping RRDtool within Shell/Perl script</h3>
<p> After understanding RRDtool it is now a time to actually use RRDtool in scripts. Tasks involved in network management are data collection, data storage, and data retrieval. In the following example, the previously created target.rrd database is used. Data collection and data storage is done using Shell scripts. Data retrieval and report generation is done using Perl scripts. These scripts are shown below: </p>
<p> <i>Shell script (collects data, updates database)</i> </p>
<pre><code>
#!/ bin / sh
a = 0 while["$a" == 0];
do
    snmpwalk - c public 192.168.1.250 hrSWRunPerfMem &gt; snmp_reply
                                                           total_mem =`awk 'BEGIN {tot_mem=0}
    {
        if ($NF == "KBytes") {
            tot_mem = tot_mem + $(NF - 1)
        }
    }
END
{
    print tot_mem
}
' snmp_reply`
#I can use N as a replacement for the current time
    rrdtool update target.rrd N : $total_mem
#sleep until the next 300 seconds are full
                                      perl -
    e 'sleep 300 - time % 300' done #end of while loop
</code></pre>
<p> <i>Perl script (retrieves data from database and generates graphs and statistics)</i> </p>
<pre><code>
#!/ usr / bin / perl - w
#This script fetches data from target.rrd, creates a graph of memory
#consumption on the target(Dual P3 Processor 1 GHz, 656 MB RAM)
#call the RRD perl module
use lib qw(/ usr / local / rrdtool - 1.0.41 / lib / perl../ lib / perl);
use RRDs;
my $cur_time = time();
#set current time
    my $end_time = $cur_time - 86400;
#set end time to 24 hours ago
    my $start_time = $end_time - 2592000;
#set start 30 days in the past
#fetch average values from the RRD database between start and end time
    my($start, $step, $ds_names, $data) =
        RRDs::fetch("target.rrd", "AVERAGE",
                    "-r", "600", "-s", "$start_time", "-e", "$end_time");
#save fetched values in a 2 - dimensional array
my $rows = 0;
my $columns = 0;
my $time_variable = $start;
foreach
    $line(@$data)
    {
        $vals[$rows][$columns] = $time_variable;
        $time_variable = $time_variable + $step;
        foreach
            $val(@$line)
            {
                $vals[$rows][++$columns] = $val;
            }
        $rows++;
        $columns = 0;
    }
my $tot_time = 0;
my $count = 0;
#save the values from the 2 - dimensional into a 1 - dimensional array
 for
     $i(0..$ #vals)
     {
         $tot_mem[$count] = $vals[$i][1];
         $count++;
     }
 my $tot_mem_sum = 0;
#calculate the total of all values
 for
     $i(0..($count - 1))
     {
         $tot_mem_sum = $tot_mem_sum + $tot_mem[$i];
     }
#calculate the average of the array
 my $tot_mem_ave = $tot_mem_sum / ($count);
#create the graph
 RRDs::graph("/images/mem_$count.png",
             "--title= Memory Usage",
             "--vertical-label=Memory Consumption (MB)",
             "--start=$start_time",
             "--end=$end_time",
             "--color=BACK#CCCCCC",
             "--color=CANVAS#CCFFFF",
             "--color=SHADEB#9999CC",
             "--height=125",
             "--upper-limit=656",
             "--lower-limit=0",
             "--rigid",
             "--base=1024",
             "DEF:tot_mem=target.rrd:mem:AVERAGE",
             "CDEF:tot_mem_cor=tot_mem,0,671744,LIMIT,UN,0,tot_mem,IF,1024,/",
             "CDEF:machine_mem=tot_mem,656,+,tot_mem,-",
             "COMMENT:Memory Consumption between $start_time",
             "COMMENT:    and $end_time                     ",
             "HRULE:656#000000:Maximum Available Memory - 656 MB",
             "AREA:machine_mem#CCFFFF:Memory Unused",
             "AREA:tot_mem_cor#6699CC:Total memory consumed in MB");
 my $err = RRDs::error;
 if ($err) {
     print "problem generating the graph: $err
";
 }
#print the output
 print "Average memory consumption is ";
 printf "%5.2f", $tot_mem_ave / 1024;
 print " MB. Graphical representation can be found at /images/mem_$count.png.";
</code></pre>
<h2>AUTHOR</h2>
<p> Ketan Patel &lt;k2pattu [at] yahoo.com&gt; </p>
<h2>Index</h2>
