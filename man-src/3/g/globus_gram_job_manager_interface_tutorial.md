---
title: "globus_gram_job_manager_interface_tutorial(3)"
name: "globus_gram_job_manager_interface_tutorial"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_job_manager_interface_tutorial/"
description: "globus_gram_job_manager_interface_tutorial – GRAM Job Manager Scheduler Tutorial This tutorial describes the steps needed to build a GRAM Job Manager Scheduler interface package."
---

<h2 class="name">NAME</h2>
<p> globus_gram_job_manager_interface_tutorial &#8211; GRAM Job Manager Scheduler Tutorial This tutorial describes the steps needed to build a GRAM Job Manager Scheduler interface package. </p>
<p> The audience for this tutorial is a person interested in adding support for a new scheduler interface to GRAM. This tutorial will assume some familiarty with GTP, autoconf, automake, and Perl. As a reference point, this tutorial will refer to the code in the LSF Job Manager package. </p>
<h2>Writing a Scheduler Interface</h2>
<p> This section deals with writing the perl module which implements the interface between the GRAM job manager and the local scheduler. Consult the <code>Job Manager Scheduler Interface</code> section of this manual for a more detailed reference on the Perl modules which are used here. </p>
<p> The scheduler interface is implemented as a Perl module which is a subclass of the Globus::GRAM::JobManager module. Its name must match the scheduler type string used when the service is installed. For the LSF scheduler, the name is <i>lsf</i>, so the module name is <i>Globus::GRAM::JobManager::lsf</i> and it is stored in the file lsf.pm. Though there are several methods in the JobManager interface, they only ones which absolutely need to be implemented in a scheduler module are submit, poll, cancel. </p>
<p> We&#8217;ll begin by looking at the start of the lsf source module, lsf.in (the transformation to lsf.pm happens when the setup script is run. To begin the script, we import the GRAM support modules into the scheduler module&#8217;s namespace, declare the module&#8217;s namespace, and declare this module as a subclass of the Globus::GRAM::JobManager module. All scheduler packages will need to do this, substituting the name of the scheduler type being implemented where we see <i>lsf</i> below. </p>
<pre><code>
use Globus::GRAM::Error;
use Globus::GRAM::JobState;
use Globus::GRAM::JobManager;
use Globus::Core::Paths;
package Globus::GRAM::JobManager::lsf;
@ISA = qw(Globus::GRAM::JobManager);
</code></pre>
<p> Next, we declare any system-specifc values which will be substituted when the setup package scripts are run. In the LSF case, we need the know the paths to a few programs which interact with the scheduler: </p>
<p>my($mpirun, $bsub, $bjobs, $bkill);<br />
BEGIN<br />
{<br />
    $mpirun = &#8216;@MPIRUN@&#8217;;<br />
    $bsub = &#8216;@BSUB@&#8217;;<br />
    $bjobs = &#8216;@BJOBS@&#8217;;<br />
    $bkill = &#8216;@BKILL@&#8217;;<br />
}</p>
<p> The values surrounded by the at-sign (such as @MPIRUN@) will be replaced by with the path to the named programs by the find-lsf-tools script described <code>below</code>.</p>
<h3>Writing a constructor</h3>
<p> For scheduler interfaces which need to setup some data before calling their other methods, they can overload the new method which acts as a constructor. Scheduler scripts which don&#8217;t need any per-instance initialization will not need to provide a constructor, the Globus::GRAM::JobManager constructor will do the job. </p>
<p> If you do need to overloaded this method, be sure to call the JobManager module&#8217;s constructor to allow it to do its initialization, as in this example: </p>
<p>sub new<br />
{<br />
    my $proto = shift;<br />
    my $class = ref($proto) || $proto;<br />
    my $self = $class-&gt;SUPER::new (@_);<br />
    ##Insert scheduler &#8211; specific startup code here return $self;<br />
}</p>
<p> The job interface methods are called with only one argument, the scheduler object itself. That object contains the a Globus::GRAM::JobDescription object ($self-&gt;{JobDescription}) which includes the values from the RSL string associated with the request, as well as a few extra values:</p>
<dl>
<dt><code>job_id </code></p>
<dd> The string returned as the value of JOB_ID in the return hash from submit. This won&#8217;t be present for methods called before the job is submitted.</p>
<dt><code>uniq_id </code></p>
<dd> A string associated with this job request by the job manager program. It will be unique for all jobs on a host for all time.</p>
<dt><code>cache_tag </code></p>
<dd> The GASS cache tag related to this job submission. Files in the cache with this tag will be cleaned by the cleanup_cache() method.</dl>
<p> Now, let&#8217;s look at the methods which will interface to the scheduler.</p>
<h3>Submitting Jobs</h3>
<p> All scheduler modules must implement the submit method. This method is called when the job manager wishes to submit the job to the scheduler. The information in the original job request RSL string is available to the scheduler interface through the JobDescription data member of it&#8217;s hash. </p>
<p> For most schedulers, this is the longest method to be implemented, as it must decide what to do with the job description, and convert them to something which the scheduler can understand. </p>
<p> We&#8217;ll look at some of the steps in the LSF manager code to see how the scheduler interface is implemented. </p>
<p> In the beginning of the submit method, we&#8217;ll get our parameters and look up the job description in the manager-specific object: </p>
<p>sub submit<br />
{<br />
    my $self = shift;<br />
    my $description = $self-&gt;{JobDescription};</p>
<p> Then we will check for values of the job parameters that we will be handling. For example, this is how we check for a valid job type in the LSF scheduler interface: </p>
<p>if(defined($description-&gt;jobtype())<br />
{<br />
    if ($description-&gt;jobtype !~ / ^(mpi | single | multiple) $ /) {<br />
        return Globus::GRAM::Error::JOBTYPE_NOT_SUPPORTED;<br />
    }<br />
    elsif($description-&gt;jobtype() eq &#8216;mpi&#8217; &amp;&amp; $mpirun eq &#8216;no&#8217;)<br />
    {<br />
        return Globus::GRAM::Error::JOBTYPE_NOT_SUPPORTED;<br />
    }<br />
}</p>
<p> The lsf module supports most of the core RSL attributes, so it does more processing to determine what to do with the values in the job description. </p>
<p> Once we&#8217;ve inspected the JobDescription we&#8217;ll know what we need to tell the scheduler about so that it&#8217;ll start the job properly. For LSF, we will construct a job description script and pass that to the bsub command. This script is a bourne shell script with some special comments which LSF uses to decide what constraints to use when scheduling the job. </p>
<p> First, we&#8217;ll open the new file, and write the file header: </p>
<p>$lsf_job_script = new IO::File($lsf_job_script_name, &#8216;&gt;&#8217;);<br />
$lsf_job_script-&gt;print &lt;&lt; EOF;<br />
#!/ bin / sh<br />
#<br />
#LSF batch job script built by Globus Job Manager<br />
#<br />
EOF</p>
<p> Then, we&#8217;ll add some special comments to pass job constraints to LSF: </p>
<p>if (defined($queue)) {<br />
    $lsf_job_script-&gt;print(&#8216;#BSUB -q $queue);<br />
}<br />
if (defined($description-&gt;project())) {<br />
    $lsf_job_script-&gt;print(&#8216;#BSUB -P &#8216; . $description-&gt;project() . &#8216;);<br />
}</p>
<p> Before we start the executable in the LSF job description script, we will quote and escape the job&#8217;s arguments so that they will be passed to the application as they were in the job submission RSL string: </p>
<p> At the end of the job description script, we actually run the executable named in the JobDescription. For LSF, we support a few different job types which require different startup commands. Here, we will quote and escape the strings in the argument list so that the values of the arguments will be identical to those in the initial job request string. For this Bourne-shell syntax script, we will double-quote each argument, and escaping the backslash (\), dollar-sign ($), double-quote (), and single-quote (&#8216;) characters. We will use this new string later in the script. </p>
<p>@arguments = $description-&gt;arguments();<br />
foreach (@arguments) {<br />
    if (ref($_)) {<br />
        return Globus::GRAM::Error::RSL_ARGUMENTS;<br />
    }<br />
}<br />
if ($arguments[0]) {<br />
    foreach (@arguments) {<br />
        $_ = ~s /\/\/ g;<br />
        $_ = ~s //\/g;<br />
                 $_ = ~s /&#8217;/\&#8217;/g; $_ = ~s /`/\`/ g;<br />
        $args.= &#8221;&#8217; . $_ . &#8216; &#8216; &#8216;;<br />
    }<br />
} else {<br />
    $args = &#8221;;<br />
}</p>
<p> To end the LSF job description script, we will write the command line of the executable to the script. Depending on the job type of this submission, we will need to start either one or more instances of the executable, or the mpirun program which will start the job with the executable count in the JobDescription: </p>
<p>if ($description-&gt;jobtype() eq &#8216;mpi&#8217;) {<br />
    $lsf_job_script-&gt;print(&#8216;$mpirun -np &#8216;.$description-&gt;count().&#8217; &#8216;);<br />
    $lsf_job_script-&gt;print($description-&gt;executable()<br />
                           . &#8216; $args );<br />
}<br />
elsif($description-&gt;jobtype() eq &#8216;multiple&#8217;)<br />
{<br />
    for (my $i = 0; $i &lt; $description-&gt;count(); $i++) {<br />
        $lsf_job_script-&gt;print($description-&gt;executable() . &#8216; $args &amp;);<br />
    }<br />
    $lsf_job_script-&gt;print(&#8216;wait);<br />
}<br />
else<br />
{<br />
    $lsf_job_script-&gt;print($description-&gt;executable() . &#8216; $args);<br />
}</p>
<p> Next, we submit the job to the scheduler. Be sure to close the script file before trying to redirect it into the submit command, or some of the script file may be buffered and things will fail in strange ways! </p>
<p> When the submission command returns, we check its output for the scheduler-specific job identifier. We will use this value to be able to poll or cancel the job. </p>
<p> The return value of the script should be either a GRAM error object or a reference to a hash of values. The Globus::GRAM::JobManager documentation lists the valid keys to that hash. For the submit method, we&#8217;ll return the job identifier as the value of JOB_ID in the hash. If the scheduler returned a job status result, we could return that as well. LSF does not, so we&#8217;ll just check for the job ID and return it, or if the job fails, we&#8217;ll return an error object: </p>
<p>$lsf_job_script-&gt;close();<br />
$job_id = (grep(/ is submitted /,<br />
                split(/, `$bsub &lt; $lsf_job_script_name`)))[0];<br />
    if($? == 0)<br />
    {<br />
        $job_id = ~m / &lt;([^ &gt; ] *)&gt; / ;<br />
        $job_id = $1;<br />
        return {JOB_ID = &gt; $job_id};<br />
    }<br />
    return Globus::GRAM::Error::INVALID_SCRIPT_REPLY;<br />
    }</p>
<p> That finishes the submit method. Most of the functionality for the scheduler interface is now written. We just have a few more (much shorter) methods to implement.</p>
<h3>Polling Jobs</h3>
<p> All scheduler modules must also implement the poll method. The purpose of this method is to check for updates of a job&#8217;s status, for example, to see if a job has finished. </p>
<p> When this method is called, we&#8217;ll get the job ID (which we returned from the submit method above) as well as the original job request information in the object&#8217;s JobDescription. In the LSF script, we&#8217;ll pass the job ID to the bjobs program, and that will return the job&#8217;s status information. We&#8217;ll compare the status field from the bjobs output to see what job state we should return. </p>
<p> If the job fails, and there is a way to determine that from the scheduler, then the script should return in its hash both </p>
<pre>
JOB_STATE =&gt; Globus::GRAM::JobState::FAILED
</pre>
<p>&nbsp;<wbr>and&nbsp;<wbr> </p>
<pre>
ERROR =&gt; Globus::GRAM::Error::&lt;ERROR_TYPE&gt;-&gt;value
</pre>
<p> Here&#8217;s an excerpt from the LSF scheduler module implementation: </p>
<p>sub poll<br />
{<br />
    my $self = shift;<br />
    my $description = $self-&gt;{JobDescription};<br />
    my $job_id = $description-&gt;jobid();<br />
    my $state;<br />
    my $status_line;<br />
    $self-&gt;log(&#8216;polling job $job_id&#8217;);<br />
#Get first line matching job id<br />
    $_ = (grep(/ $job_id /, `$bjobs $job_id 2 &gt; / dev / null`))[0];<br />
#Get 3th field(status)<br />
    $_ = (split(//))[2];<br />
    if(/PEND/)<br />
    {<br />
        $state = Globus::GRAM::JobState::PENDING;<br />
    }<br />
    elsif(/USUSP|SSUSP|PSUSP/)<br />
    {<br />
        $state = Globus::GRAM::JobState::SUSPENDED<br />
    }<br />
    &#8230;<br />
    return {JOB_STATE =&gt; $state};<br />
}</p>
<h3>Cancelling Jobs</h3>
<p> All scheduler modules must also implement the cancel method. The purpose of this method is to cancel a running job. </p>
<p> As with the poll method described above, this method will be given the job ID as part of the JobDescription object held by the manager object. If the scheduler interface provides feedback that the job was cancelled successfully, then we can return a JOB_STATE change to the FAILED state. Otherwise we can return an empty hash reference, and let the poll method return the state change next time it is called. </p>
<p> To process a cancel in the LSF case, we will run the bkill command with the job ID. </p>
<p>sub cancel<br />
{<br />
    my $self = shift;<br />
    my $description = $self-&gt;{JobDescription};<br />
    my $job_id = $description-&gt;jobid();<br />
    $self-&gt;log(&#8216;cancel job $job_id&#8217;);<br />
    system(&#8216;$bkill $job_id &gt;/dev/null 2&gt;/dev/null&#8217;);<br />
    if($? == 0)<br />
    {<br />
        return<br />
        {<br />
            JOB_STATE = &gt; Globus::GRAM::JobState::FAILED<br />
        }<br />
    }<br />
    return Globus::GRAM::Error::JOB_CANCEL_FAILED;<br />
}</p>
<h3>End of the script</h3>
<p> It is required that all perl modules return a non-zero value when they are parsed. To do this, make sure the last line of your module consists of: </p>
<pre>
1;
</pre>
<h2>Setting up a Scheduler</h2>
<p> Once we&#8217;ve written the job manager script, we need to get it installed so that the gatekeeper will be able to run our new service. We do this by writing a setup script. For LSF, we will write the script setup-globus-job-manager-lsf.pl, which we will list in the LSF package as the <code>Post_Install_Program</code>. </p>
<p> To set up the Gatekeeper service, our LSF setup script does the following:</p>
<dl>
<dt>1.</p>
<dd> Perform system-specific configuration.</p>
<dt>2.</p>
<dd> Install the GRAM scheduler Perl module and register as a gatekeeper service.</p>
<dt>3.</p>
<dd> <code>(Optional)</code> Install an RSL validation file defining extra scheduler-specific RSL attributes which the scheduler interface will support.</p>
<dt>4.</p>
<dd> Update the GPT metadata to indicate that the job manager service has been set up.</dl>
<h3>System-Specific Configuration</h3>
<p> First, our scheduler setup script probes for any system-specific information needed to interface with the local scheduler. For example, the LSF scheduler uses the mpirun, bsub, bqueues, bjobs, and bkill commands to submit, poll, and cancel jobs. We&#8217;ll assume that the administrator who is installing the package has these commands in their path. We&#8217;ll use an autoconf script to locate the executable paths for these commands and substitute them into our scheduler Perl module. In the LSF package, we have the find-lsf-tools script, which is generated during bootstrap by autoconf from the find-lsf-tools.in file: </p>
<p>##Required Prolog<br />
    AC_REVISION($Revision : 1.5 $)<br />
        AC_INIT(lsf.in)<br />
#checking for the GLOBUS_LOCATION<br />
            if test &#8216;x$GLOBUS_LOCATION&#8217; = &#8216;x&#8217;; then<br />
    echo &#8216;ERROR Please specify GLOBUS_LOCATION&#8217; &gt;&amp;2<br />
    exit 1<br />
fi<br />
## Check for optional tools, warn if not found<br />
AC_PATH_PROG(MPIRUN, mpirun, no)<br />
if test &#8216;$MPIRUN&#8217; = &#8216;no&#8217; ; then<br />
    AC_MSG_WARN([Cannot locate mpirun])<br />
fi<br />
## Check for required tools, error if not found<br />
AC_PATH_PROG(BSUB, bsub, no)<br />
if test &#8216;$BSUB&#8217; = &#8216;no&#8217; ;<br />
then<br />
        AC_MSG_ERROR([Cannot locate bsub])<br />
            fi<br />
    ##Required epilog<br />
    &#8211; update scheduler specific module<br />
    prefix = &#8216;$(GLOBUS_LOCATION)&#8217; exec_prefix = &#8216;$(GLOBUS_LOCATION)&#8217; libexecdir = ${prefix} / libexec<br />
                                                                                  AC_OUTPUT(<br />
                                                                                      lsf.pm<br />
                                                                                      : lsf.in)</p>
<p> If this script exits with a non-zero error code, then the setup script propagates the error to the caller and exits without installing the service.</p>
<h3>Registering as a Gatekeeper Service</h3>
<p> Next, the setup script installs it&#8217;s perl module into the perl library directory and registers an entry in the Globus Gatekeeper&#8217;s service directory. The program globus-job-manager-service (distributed in the job manager program setup package) performs both of these tasks. When run, it expects the scheduler perl module to be located in the $GLOBUS_LOCATION/setup/globus directory. </p>
<pre>
$libexecdir/globus-job-manager-service -add -m lsf -s jobmanager-lsf;
</pre>
<h3>Installing an RSL Validation File</h3>
<p> If the scheduler script implements RSL attributes which are not part of the core set supported by the job manager, it must publish them in the job manager&#8217;s data directory. If the scheduler script wants to set some default values of RSL attributes, it may also set those as the default values in the validation file. </p>
<p> The format of the validation file is described in the <code>RSL Validation File Format</code> section of the documentation. The validation file must be named <i>scheduler-type</i>.rvf and installed in the $GLOBUS_LOCATION/share/globus_gram_job_manager directory. </p>
<p> In the LSF setup script, we check the list of queues supported by the local LSF installation, and add a section of acceptable values for the <i>queue</i> RSL attribute: </p>
<p>open(VALIDATION_FILE,<br />
     &#8216;&gt;$ENV{GLOBUS_LOCATION}/share/globus_gram_job_manager/lsf.rvf&#8217;);<br />
#Customize validation file with queue info<br />
open(BQUEUES, &#8216;bqueues -w |&#8217;);<br />
#discard header<br />
$_ = &lt;BQUEUES&gt;;<br />
my @queues = ();<br />
while (&lt;BQUEUES&gt;) {<br />
    chomp;<br />
    $_ = ~m / ^(S +) / ;<br />
    push(@queues, $1);<br />
}<br />
close(BQUEUES);<br />
if (@queues) {<br />
    print VALIDATION_FILE &#8216;Attribute: queue; print VALIDATION_FILE join(&#8216; &#8216;, &#8216;Values:&#8217;, @queues);<br />
}<br />
close VALIDATION_FILE;</p>
<h3>Updating GPT Metadata</h3>
<p> Finally, the setup package should create and finalize a Grid::GPT::Setup. The value of $package must be the same value as the gpt_package_metadata <i>Name</i> attribute in the package&#8217;s metadata file. If either the new() or finish() methods fail, then it is considered good practice to clean up any files created by the setup script. From setup-globus-job-manager-lsf.pl: </p>
<p>my $metadata =<br />
    new Grid::GPT::Setup(<br />
        package_name = &gt; &#8216;globus_gram_job_manager_setup_lsf&#8217;);<br />
$metadata-&gt;finish();</p>
<h2>Packaging</h2>
<p> Now that we&#8217;ve written a job manager scheduler interface, we&#8217;ll package it using GPT to make it easy for our users to build and install. We&#8217;ll start by gathering the different files we&#8217;ve written above into a single directory lsf.</p>
<dl>
<dt>*</p>
<dd> lsf.in</p>
<dt>*</p>
<dd> find-lsf-tools.in</p>
<dt>*</p>
<dd> setup-globus-job-manager.pl</dl>
<h3>Package Documentation</h3>
<p> If there are any scheduler-specific options defined for this scheduler module, or if there any any optional setup items, then it is good to provide a documentation page which describes these. For LSF, we describe the changes since the last version of this package in the file globus_gram_job_manager_lsf.dox. This file consists of a doxygen mainpage. See <a rel="nofollow" href="http://www.doxygen.org">www.doxygen.org</a> for information on how to write documentation with that tool.</p>
<h3>configure.in</h3>
<p> Now, we&#8217;ll write our configure.in script. This file is converted to the configure shell script by the bootstrap script below. Since we don&#8217;t do any probes for compile-time tools or system characteristics, we just call the various initialization macros used by GPT, declare that we may provide doxygen documentation, and then output the files we need substitions done on. </p>
<pre>
AC_REVISION($Revision: 1.5 $)
AC_INIT(Makefile.am)
GLOBUS_INIT
AM_PROG_LIBTOOL
dnl Initialize the automake rules the last argument
AM_INIT_AUTOMAKE($GPT_NAME, $GPT_VERSION)
LAC_DOXYGEN('../', '*.dox')
GLOBUS_FINALIZE
AC_OUTPUT(
        Makefile
        pkgdata/Makefile
        pkgdata/pkg_data_src.gpt
        doxygen/Doxyfile
        doxygen/Doxyfile-internal
        doxygen/Makefile
)
</pre>
<h3>Package Metadata</h3>
<p> Now we&#8217;ll write our metadata file, and put it in the pkgdata subdirectory of our package. The important things to note in this file are the package name and version, the post_install_program, and the setup sections. These define how the package distribution will be named, what command will be run by gpt-postinstall when this package is installed, and what the setup dependencies will be written when the Grid::GPT::Setup object is <code>finalized</code>. </p>
<pre>
&lt;?xml version='1.0' encoding='UTF-8'?&gt;
&lt;!DOCTYPE gpt_package_metadata SYSTEM 'package.dtd'&gt;
&lt;gpt_package_metadata Format_Version='0.02' Name='globus_gram_job_manager_setup_lsf' &gt;
  &lt;Aging_Version Age='0' Major='1' Minor='0' /&gt;
  &lt;Description &gt;LSF Job Manager Setup&lt;/Description&gt;
  &lt;Functional_Group &gt;ResourceManagement&lt;/Functional_Group&gt;
  &lt;Version_Stability Release='Beta' /&gt;
  &lt;src_pkg &gt;
    &lt;With_Flavors build='no' /&gt;
    &lt;Source_Setup_Dependency PkgType='pgm' &gt;
      &lt;Setup_Dependency Name='globus_gram_job_manager_setup' &gt;
        &lt;Version &gt;
          &lt;Simple_Version Major='3' /&gt;
        &lt;/Version&gt;
      &lt;/Setup_Dependency&gt;
      &lt;Setup_Dependency Name='globus_common_setup' &gt;
        &lt;Version &gt;
          &lt;Simple_Version Major='2' /&gt;
        &lt;/Version&gt;
      &lt;/Setup_Dependency&gt;
    &lt;/Source_Setup_Dependency&gt;
    &lt;Build_Environment &gt;
      &lt;cflags &gt;@GPT_CFLAGS@&lt;/cflags&gt;
      &lt;external_includes &gt;@GPT_EXTERNAL_INCLUDES@&lt;/external_includes&gt;
      &lt;pkg_libs &gt; &lt;/pkg_libs&gt;
      &lt;external_libs &gt;@GPT_EXTERNAL_LIBS@&lt;/external_libs&gt;
    &lt;/Build_Environment&gt;
    &lt;Post_Install_Message &gt;
      Run the setup-globus-job-manager-lsf setup script to configure an
      lsf job manager.
    &lt;/Post_Install_Message&gt;
    &lt;Post_Install_Program &gt;
      setup-globus-job-manager-lsf
    &lt;/Post_Install_Program&gt;
    &lt;Setup Name='globus_gram_job_manager_service_setup' &gt;
      &lt;Aging_Version Age='0' Major='1' Minor='0' /&gt;
    &lt;/Setup&gt;
  &lt;/src_pkg&gt;
&lt;/gpt_package_metadata&gt;
</pre>
<h3>Automake Makefile.am</h3>
<p> The automake Makefile.am for this package is short because there isn&#8217;t any compilation needed for this package. We just need to define what needs to be installed into which directory, and what source files need to be put inot our source distribution. For the LSF package, we need to list the lsf.in, find-lsf-tools, and setup-globus-job-manager-lsf.pl scripts as files to be installed into the setup directory. We need to add those files plus our documentation source file to the EXTRA_LIST variable so that they will be included in source distributions. The rest of the lines in the file are needed for proper interaction with GPT. </p>
<p>include $(top_srcdir) / globus_automake_pre include $(top_srcdir) / globus_automake_pre_top SUBDIRS = pkgdata doxygen<br />
    setup_SCRIPTS = lsf.in find &#8211; lsf &#8211; tools setup &#8211; globus &#8211; job &#8211; manager &#8211; lsf.pl EXTRA_DIST = $(setup_SCRIPTS) globus_gram_job_manager_lsf.dox<br />
                                                                                                   include $(top_srcdir) /<br />
                                                                                                   globus_automake_post<br />
                                                                                                   include $(top_srcdir) /<br />
                                                                                                   globus_automake_post_top</p>
<h3>Bootstrap</h3>
<p> The final piece we need to write for our package is the bootstrap script. This script is the standard bootstrap script for a globus package, with an extra line to generate the fine-lsf-tools script using autoconf. </p>
<p>#!/ bin / sh<br />
#checking for the GLOBUS_LOCATION<br />
if test<br />
    &#8216;x$GLOBUS_LOCATION&#8217; = &#8216;x&#8217;;<br />
then<br />
        echo &#8216;ERROR Please specify GLOBUS_LOCATION&#8217; &gt; &amp;2 exit 1 fi if[!-f ${GLOBUS_LOCATION} / libexec / globus &#8211; bootstrap.sh];<br />
then<br />
            echo &#8216;ERROR: Unable to locate {GLOBUS_LOCATION}/libexec/globus-bootstrap.sh&#8217; echo &#8216;       Please ensure that you have installed the globus-core package and&#8217; echo &#8216;       that GLOBUS_LOCATION is set to the proper directory&#8217; exit<br />
                fi<br />
                    autoconf find &#8211;<br />
        lsf &#8211; tools.in &gt;<br />
    find &#8211; lsf &#8211; tools chmod 755 find &#8211; lsf &#8211; tools exit 0</p>
<h2>Building, Testing, and Debugging</h2>
<p> With this all done, we can now try to build our now package. To do so, we&#8217;ll need to run </p>
<pre>
% ./bootstrap
% ./globus-build
</pre>
<p> If all of the files are written correctly, this should result in our package being installed into $GLOBUS_LOCATION. Once that is done, we should be able to run gpt-postinstall to configure our new job manager. </p>
<p> Now, we should be able to run the command </p>
<pre>
% globus-personal-gatekeeper -start -jmtype lsf
</pre>
<p> to start a gatekeeper configured to run a job manager using our new scripts. Running this will output a contact string (referred to as &lt;contact-string&gt; below), which we can use to connect to this new service. To do so, we&#8217;ll run globus-job-run to submit a test job: </p>
<pre>
% globus-job-run &lt;contact-string&gt; /bin/echo Hello, LSF
Hello, LSF
</pre>
<h3>When Things Go Wrong</h3>
<p> If the test above fails, or more complicated job failures are occurring, then you&#8217;lll have to debug your scheduler interface. Here are a few tips to help you out. </p>
<p> Make sure that your script is valid Perl. If you run </p>
<pre>
perl -I$GLOBUS_LOCATION/lib/perl     $GLOBUS_LOCATION/lib/perl/Globus/GRAM/JobManager/lsf.pm
</pre>
<p> You should get no output. If there are any diagnostics, correct them (in the lsf.in file), reinstall your package, and rerun the setup script. </p>
<p> Look at the Globus Toolkit Error FAQ and see if the failure is perhaps not related to your scheduler script at all. </p>
<p> Enable logging for the job manager. By default, the job manager is configured to log only when it notices a job failure. However, if your problem is that your script is not returning a failure code when you expect, you might want to enable logging always. To do this, modify the job manager configuration file to contain &#8216;-save-logfile&amp;nbsp;always&#8217; in place of &#8216;-save-log&amp;nbsp;on_error&#8217;. </p>
<p> Adding logging messages to your script: the JobManager object implements a log method, which allows you to write messages to the job manager log file. Do this as your methods are called to pinpoint where the error occurs. </p>
<p> Save the job description file when your script is run. This will allow you to run the globus-job-manager-script.pl interactively (or in the Perl debugger). To save the job description file, you can do </p>
<pre><code>
$self-&gt;
{
    JobDescription
    } -&gt; save('/tmp/job_description.$$');
</code></pre>
<p> in any of the methods you&#8217;ve implemented. </p>
<h2>Index</h2>
