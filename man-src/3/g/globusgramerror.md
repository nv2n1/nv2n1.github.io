---
title: "globusgramerror(3)"
name: "globusgramerror"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globusgramerror/"
---

Globus::GRAM::Error - GRAM Protocol Error Constants 

<h2>Description</h2>The Globus::GRAM::Error module defines symbolic names for the Error constants in the <font SIZE="-1">GRAM</font> Protocol. 

 The Globus::GRAM::Error module methods return an object consisting of an integer erorr code, and (optionally) a string explaining the error.
<h2>Methods</h2><dl COMPACT><dt>$error = new Globus::GRAM::Error($number, <tt>$string);
<dd>Create a new error object with the given error number and string description. This is called by the error-specific factory methods described below.
<dt>$error</tt>-&gt;<i>string()
<dd>Return the error string associated with a Globus::GRAM::Error object.
<dt>$error</i>-&gt;<i>value()
<dd>Return the integer error code associated with a Globus::GRAM::Error object.
<dt>$error</i> = <i>Globus::GRAM::Error::PARAMETER_NOT_SUPPORTED()
<dd>Create a new </i><font SIZE="-1"><i>PARAMETER_NOT_SUPPORTED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_REQUEST()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_REQUEST</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::NO_RESOURCES()
<dd>Create a new </i><font SIZE="-1"><i>NO_RESOURCES</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::BAD_DIRECTORY()
<dd>Create a new </i><font SIZE="-1"><i>BAD_DIRECTORY</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::EXECUTABLE_NOT_FOUND()
<dd>Create a new </i><font SIZE="-1"><i>EXECUTABLE_NOT_FOUND</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INSUFFICIENT_FUNDS()
<dd>Create a new </i><font SIZE="-1"><i>INSUFFICIENT_FUNDS</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::AUTHORIZATION()
<dd>Create a new </i><font SIZE="-1"><i>AUTHORIZATION</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::USER_CANCELLED()
<dd>Create a new </i><font SIZE="-1"><i>USER_CANCELLED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::SYSTEM_CANCELLED()
<dd>Create a new </i><font SIZE="-1"><i>SYSTEM_CANCELLED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::PROTOCOL_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>PROTOCOL_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::STDIN_NOT_FOUND()
<dd>Create a new </i><font SIZE="-1"><i>STDIN_NOT_FOUND</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::CONNECTION_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>CONNECTION_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_MAXTIME()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_MAXTIME</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_COUNT()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_COUNT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::NULL_SPECIFICATION_TREE()
<dd>Create a new </i><font SIZE="-1"><i>NULL_SPECIFICATION_TREE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::JM_FAILED_ALLOW_ATTACH()
<dd>Create a new </i><font SIZE="-1"><i>JM_FAILED_ALLOW_ATTACH</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::JOB_EXECUTION_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>JOB_EXECUTION_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_PARADYN()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_PARADYN</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_JOBTYPE()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_JOBTYPE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_GRAM_MYJOB()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_GRAM_MYJOB</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::BAD_SCRIPT_ARG_FILE()
<dd>Create a new </i><font SIZE="-1"><i>BAD_SCRIPT_ARG_FILE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::ARG_FILE_CREATION_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>ARG_FILE_CREATION_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_JOBSTATE()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_JOBSTATE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_SCRIPT_REPLY()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_SCRIPT_REPLY</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_SCRIPT_STATUS()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_SCRIPT_STATUS</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::JOBTYPE_NOT_SUPPORTED()
<dd>Create a new </i><font SIZE="-1"><i>JOBTYPE_NOT_SUPPORTED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::UNIMPLEMENTED()
<dd>Create a new </i><font SIZE="-1"><i>UNIMPLEMENTED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::TEMP_SCRIPT_FILE_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>TEMP_SCRIPT_FILE_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::USER_PROXY_NOT_FOUND()
<dd>Create a new </i><font SIZE="-1"><i>USER_PROXY_NOT_FOUND</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::OPENING_USER_PROXY()
<dd>Create a new </i><font SIZE="-1"><i>OPENING_USER_PROXY</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::JOB_CANCEL_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>JOB_CANCEL_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::MALLOC_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>MALLOC_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::DUCT_INIT_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>DUCT_INIT_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::DUCT_LSP_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>DUCT_LSP_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_HOST_COUNT()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_HOST_COUNT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::UNSUPPORTED_PARAMETER()
<dd>Create a new </i><font SIZE="-1"><i>UNSUPPORTED_PARAMETER</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_QUEUE()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_QUEUE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_PROJECT()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_PROJECT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_EVALUATION_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>RSL_EVALUATION_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::BAD_RSL_ENVIRONMENT()
<dd>Create a new </i><font SIZE="-1"><i>BAD_RSL_ENVIRONMENT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::DRYRUN()
<dd>Create a new </i><font SIZE="-1"><i>DRYRUN</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::ZERO_LENGTH_RSL()
<dd>Create a new </i><font SIZE="-1"><i>ZERO_LENGTH_RSL</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::STAGING_EXECUTABLE()
<dd>Create a new </i><font SIZE="-1"><i>STAGING_EXECUTABLE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::STAGING_STDIN()
<dd>Create a new </i><font SIZE="-1"><i>STAGING_STDIN</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_JOB_MANAGER_TYPE()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_JOB_MANAGER_TYPE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::BAD_ARGUMENTS()
<dd>Create a new </i><font SIZE="-1"><i>BAD_ARGUMENTS</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::GATEKEEPER_MISCONFIGURED()
<dd>Create a new </i><font SIZE="-1"><i>GATEKEEPER_MISCONFIGURED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::BAD_RSL()
<dd>Create a new </i><font SIZE="-1"><i>BAD_RSL</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::VERSION_MISMATCH()
<dd>Create a new </i><font SIZE="-1"><i>VERSION_MISMATCH</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_ARGUMENTS()
<dd>Create a new </i><font SIZE="-1"><i>RSL_ARGUMENTS</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_COUNT()
<dd>Create a new </i><font SIZE="-1"><i>RSL_COUNT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_DIRECTORY()
<dd>Create a new </i><font SIZE="-1"><i>RSL_DIRECTORY</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_DRYRUN()
<dd>Create a new </i><font SIZE="-1"><i>RSL_DRYRUN</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_ENVIRONMENT()
<dd>Create a new </i><font SIZE="-1"><i>RSL_ENVIRONMENT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_EXECUTABLE()
<dd>Create a new </i><font SIZE="-1"><i>RSL_EXECUTABLE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_HOST_COUNT()
<dd>Create a new </i><font SIZE="-1"><i>RSL_HOST_COUNT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_JOBTYPE()
<dd>Create a new </i><font SIZE="-1"><i>RSL_JOBTYPE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_MAXTIME()
<dd>Create a new </i><font SIZE="-1"><i>RSL_MAXTIME</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_MYJOB()
<dd>Create a new </i><font SIZE="-1"><i>RSL_MYJOB</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_PARADYN()
<dd>Create a new </i><font SIZE="-1"><i>RSL_PARADYN</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_PROJECT()
<dd>Create a new </i><font SIZE="-1"><i>RSL_PROJECT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_QUEUE()
<dd>Create a new </i><font SIZE="-1"><i>RSL_QUEUE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_STDERR()
<dd>Create a new </i><font SIZE="-1"><i>RSL_STDERR</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_STDIN()
<dd>Create a new </i><font SIZE="-1"><i>RSL_STDIN</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_STDOUT()
<dd>Create a new </i><font SIZE="-1"><i>RSL_STDOUT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::OPENING_JOBMANAGER_SCRIPT()
<dd>Create a new </i><font SIZE="-1"><i>OPENING_JOBMANAGER_SCRIPT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::CREATING_PIPE()
<dd>Create a new </i><font SIZE="-1"><i>CREATING_PIPE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::FCNTL_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>FCNTL_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::STDOUT_FILENAME_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>STDOUT_FILENAME_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::STDERR_FILENAME_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>STDERR_FILENAME_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::FORKING_EXECUTABLE()
<dd>Create a new </i><font SIZE="-1"><i>FORKING_EXECUTABLE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::EXECUTABLE_PERMISSIONS()
<dd>Create a new </i><font SIZE="-1"><i>EXECUTABLE_PERMISSIONS</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::OPENING_STDOUT()
<dd>Create a new </i><font SIZE="-1"><i>OPENING_STDOUT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::OPENING_STDERR()
<dd>Create a new </i><font SIZE="-1"><i>OPENING_STDERR</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::OPENING_CACHE_USER_PROXY()
<dd>Create a new </i><font SIZE="-1"><i>OPENING_CACHE_USER_PROXY</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::OPENING_CACHE()
<dd>Create a new </i><font SIZE="-1"><i>OPENING_CACHE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INSERTING_CLIENT_CONTACT()
<dd>Create a new </i><font SIZE="-1"><i>INSERTING_CLIENT_CONTACT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::CLIENT_CONTACT_NOT_FOUND()
<dd>Create a new </i><font SIZE="-1"><i>CLIENT_CONTACT_NOT_FOUND</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::CONTACTING_JOB_MANAGER()
<dd>Create a new </i><font SIZE="-1"><i>CONTACTING_JOB_MANAGER</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_JOB_CONTACT()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_JOB_CONTACT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::UNDEFINED_EXE()
<dd>Create a new </i><font SIZE="-1"><i>UNDEFINED_EXE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::CONDOR_ARCH()
<dd>Create a new </i><font SIZE="-1"><i>CONDOR_ARCH</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::CONDOR_OS()
<dd>Create a new </i><font SIZE="-1"><i>CONDOR_OS</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_MIN_MEMORY()
<dd>Create a new </i><font SIZE="-1"><i>RSL_MIN_MEMORY</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_MAX_MEMORY()
<dd>Create a new </i><font SIZE="-1"><i>RSL_MAX_MEMORY</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_MIN_MEMORY()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_MIN_MEMORY</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_MAX_MEMORY()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_MAX_MEMORY</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::HTTP_FRAME_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>HTTP_FRAME_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::HTTP_UNFRAME_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>HTTP_UNFRAME_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::HTTP_PACK_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>HTTP_PACK_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::HTTP_UNPACK_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>HTTP_UNPACK_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_JOB_QUERY()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_JOB_QUERY</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::SERVICE_NOT_FOUND()
<dd>Create a new </i><font SIZE="-1"><i>SERVICE_NOT_FOUND</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::JOB_QUERY_DENIAL()
<dd>Create a new </i><font SIZE="-1"><i>JOB_QUERY_DENIAL</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::CALLBACK_NOT_FOUND()
<dd>Create a new </i><font SIZE="-1"><i>CALLBACK_NOT_FOUND</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::BAD_GATEKEEPER_CONTACT()
<dd>Create a new </i><font SIZE="-1"><i>BAD_GATEKEEPER_CONTACT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::POE_NOT_FOUND()
<dd>Create a new </i><font SIZE="-1"><i>POE_NOT_FOUND</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::MPIRUN_NOT_FOUND()
<dd>Create a new </i><font SIZE="-1"><i>MPIRUN_NOT_FOUND</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_START_TIME()
<dd>Create a new </i><font SIZE="-1"><i>RSL_START_TIME</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_RESERVATION_HANDLE()
<dd>Create a new </i><font SIZE="-1"><i>RSL_RESERVATION_HANDLE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_MAX_WALL_TIME()
<dd>Create a new </i><font SIZE="-1"><i>RSL_MAX_WALL_TIME</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_MAX_WALL_TIME()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_MAX_WALL_TIME</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_MAX_CPU_TIME()
<dd>Create a new </i><font SIZE="-1"><i>RSL_MAX_CPU_TIME</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_MAX_CPU_TIME()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_MAX_CPU_TIME</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::JM_SCRIPT_NOT_FOUND()
<dd>Create a new </i><font SIZE="-1"><i>JM_SCRIPT_NOT_FOUND</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::JM_SCRIPT_PERMISSIONS()
<dd>Create a new </i><font SIZE="-1"><i>JM_SCRIPT_PERMISSIONS</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::SIGNALING_JOB()
<dd>Create a new </i><font SIZE="-1"><i>SIGNALING_JOB</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::UNKNOWN_SIGNAL_TYPE()
<dd>Create a new </i><font SIZE="-1"><i>UNKNOWN_SIGNAL_TYPE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::GETTING_JOBID()
<dd>Create a new </i><font SIZE="-1"><i>GETTING_JOBID</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::WAITING_FOR_COMMIT()
<dd>Create a new </i><font SIZE="-1"><i>WAITING_FOR_COMMIT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::COMMIT_TIMED_OUT()
<dd>Create a new </i><font SIZE="-1"><i>COMMIT_TIMED_OUT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_SAVE_STATE()
<dd>Create a new </i><font SIZE="-1"><i>RSL_SAVE_STATE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_RESTART()
<dd>Create a new </i><font SIZE="-1"><i>RSL_RESTART</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_TWO_PHASE_COMMIT()
<dd>Create a new </i><font SIZE="-1"><i>RSL_TWO_PHASE_COMMIT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_TWO_PHASE_COMMIT()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_TWO_PHASE_COMMIT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_STDOUT_POSITION()
<dd>Create a new </i><font SIZE="-1"><i>RSL_STDOUT_POSITION</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_STDOUT_POSITION()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_STDOUT_POSITION</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_STDERR_POSITION()
<dd>Create a new </i><font SIZE="-1"><i>RSL_STDERR_POSITION</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_STDERR_POSITION()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_STDERR_POSITION</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RESTART_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>RESTART_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::NO_STATE_FILE()
<dd>Create a new </i><font SIZE="-1"><i>NO_STATE_FILE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::READING_STATE_FILE()
<dd>Create a new </i><font SIZE="-1"><i>READING_STATE_FILE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::WRITING_STATE_FILE()
<dd>Create a new </i><font SIZE="-1"><i>WRITING_STATE_FILE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::OLD_JM_ALIVE()
<dd>Create a new </i><font SIZE="-1"><i>OLD_JM_ALIVE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::TTL_EXPIRED()
<dd>Create a new </i><font SIZE="-1"><i>TTL_EXPIRED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::SUBMIT_UNKNOWN()
<dd>Create a new </i><font SIZE="-1"><i>SUBMIT_UNKNOWN</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_REMOTE_IO_URL()
<dd>Create a new </i><font SIZE="-1"><i>RSL_REMOTE_IO_URL</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::WRITING_REMOTE_IO_URL()
<dd>Create a new </i><font SIZE="-1"><i>WRITING_REMOTE_IO_URL</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::STDIO_SIZE()
<dd>Create a new </i><font SIZE="-1"><i>STDIO_SIZE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::JM_STOPPED()
<dd>Create a new </i><font SIZE="-1"><i>JM_STOPPED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::USER_PROXY_EXPIRED()
<dd>Create a new </i><font SIZE="-1"><i>USER_PROXY_EXPIRED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::JOB_UNSUBMITTED()
<dd>Create a new </i><font SIZE="-1"><i>JOB_UNSUBMITTED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_COMMIT()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_COMMIT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_SCHEDULER_SPECIFIC()
<dd>Create a new </i><font SIZE="-1"><i>RSL_SCHEDULER_SPECIFIC</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::STAGE_IN_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>STAGE_IN_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_SCRATCH()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_SCRATCH</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_CACHE()
<dd>Create a new </i><font SIZE="-1"><i>RSL_CACHE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_SUBMIT_ATTRIBUTE()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_SUBMIT_ATTRIBUTE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_STDIO_UPDATE_ATTRIBUTE()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_STDIO_UPDATE_ATTRIBUTE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_RESTART_ATTRIBUTE()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_RESTART_ATTRIBUTE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_FILE_STAGE_IN()
<dd>Create a new </i><font SIZE="-1"><i>RSL_FILE_STAGE_IN</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_FILE_STAGE_IN_SHARED()
<dd>Create a new </i><font SIZE="-1"><i>RSL_FILE_STAGE_IN_SHARED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_FILE_STAGE_OUT()
<dd>Create a new </i><font SIZE="-1"><i>RSL_FILE_STAGE_OUT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_GASS_CACHE()
<dd>Create a new </i><font SIZE="-1"><i>RSL_GASS_CACHE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_FILE_CLEANUP()
<dd>Create a new </i><font SIZE="-1"><i>RSL_FILE_CLEANUP</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_SCRATCH()
<dd>Create a new </i><font SIZE="-1"><i>RSL_SCRATCH</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_SCHEDULER_SPECIFIC()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_SCHEDULER_SPECIFIC</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::UNDEFINED_ATTRIBUTE()
<dd>Create a new </i><font SIZE="-1"><i>UNDEFINED_ATTRIBUTE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_CACHE()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_CACHE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_SAVE_STATE()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_SAVE_STATE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::OPENING_VALIDATION_FILE()
<dd>Create a new </i><font SIZE="-1"><i>OPENING_VALIDATION_FILE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::READING_VALIDATION_FILE()
<dd>Create a new </i><font SIZE="-1"><i>READING_VALIDATION_FILE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_PROXY_TIMEOUT()
<dd>Create a new </i><font SIZE="-1"><i>RSL_PROXY_TIMEOUT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_PROXY_TIMEOUT()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_PROXY_TIMEOUT</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::STAGE_OUT_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>STAGE_OUT_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::JOB_CONTACT_NOT_FOUND()
<dd>Create a new </i><font SIZE="-1"><i>JOB_CONTACT_NOT_FOUND</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::DELEGATION_FAILED()
<dd>Create a new </i><font SIZE="-1"><i>DELEGATION_FAILED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::LOCKING_STATE_LOCK_FILE()
<dd>Create a new </i><font SIZE="-1"><i>LOCKING_STATE_LOCK_FILE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_ATTR()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_ATTR</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::NULL_PARAMETER()
<dd>Create a new </i><font SIZE="-1"><i>NULL_PARAMETER</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::STILL_STREAMING()
<dd>Create a new </i><font SIZE="-1"><i>STILL_STREAMING</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::AUTHORIZATION_DENIED()
<dd>Create a new </i><font SIZE="-1"><i>AUTHORIZATION_DENIED</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::AUTHORIZATION_SYSTEM_FAILURE()
<dd>Create a new </i><font SIZE="-1"><i>AUTHORIZATION_SYSTEM_FAILURE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::AUTHORIZATION_DENIED_JOB_ID()
<dd>Create a new </i><font SIZE="-1"><i>AUTHORIZATION_DENIED_JOB_ID</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::AUTHORIZATION_DENIED_EXECUTABLE()
<dd>Create a new </i><font SIZE="-1"><i>AUTHORIZATION_DENIED_EXECUTABLE</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::RSL_USER_NAME()
<dd>Create a new </i><font SIZE="-1"><i>RSL_USER_NAME</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::INVALID_USER_NAME()
<dd>Create a new </i><font SIZE="-1"><i>INVALID_USER_NAME</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error.
<dt>$error</i> = <i>Globus::GRAM::Error::LAST()
<dd>Create a new </i><font SIZE="-1"><i>LAST</i></font><i> </i><font SIZE="-1"><i>GRAM</i></font><i> error. 

</dl>
 </i>
