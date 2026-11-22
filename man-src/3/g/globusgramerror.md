---
title: "globusgramerror(3)"
name: "globusgramerror"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globusgramerror/"
---

Globus::GRAM::Error - GRAM Protocol Error Constants 

<h2>Description</h2>The Globus::GRAM::Error module defines symbolic names for the Error constants in the GRAM Protocol. 

 The Globus::GRAM::Error module methods return an object consisting of an integer erorr code, and (optionally) a string explaining the error.
<h2>Methods</h2><dl COMPACT><dt>$error = new Globus::GRAM::Error($number, <tt>$string);
</dt><dd>Create a new error object with the given error number and string description. This is called by the error-specific factory methods described below.
</dd><dt>$error</tt>-&gt;<i>string()
</dt><dd>Return the error string associated with a Globus::GRAM::Error object.
</dd><dt>$error</i>-&gt;<i>value()
</dt><dd>Return the integer error code associated with a Globus::GRAM::Error object.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::PARAMETER_NOT_SUPPORTED()
</dt><dd>Create a new </i><i>PARAMETER_NOT_SUPPORTED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_REQUEST()
</dt><dd>Create a new </i><i>INVALID_REQUEST</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::NO_RESOURCES()
</dt><dd>Create a new </i><i>NO_RESOURCES</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::BAD_DIRECTORY()
</dt><dd>Create a new </i><i>BAD_DIRECTORY</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::EXECUTABLE_NOT_FOUND()
</dt><dd>Create a new </i><i>EXECUTABLE_NOT_FOUND</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INSUFFICIENT_FUNDS()
</dt><dd>Create a new </i><i>INSUFFICIENT_FUNDS</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::AUTHORIZATION()
</dt><dd>Create a new </i><i>AUTHORIZATION</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::USER_CANCELLED()
</dt><dd>Create a new </i><i>USER_CANCELLED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::SYSTEM_CANCELLED()
</dt><dd>Create a new </i><i>SYSTEM_CANCELLED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::PROTOCOL_FAILED()
</dt><dd>Create a new </i><i>PROTOCOL_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::STDIN_NOT_FOUND()
</dt><dd>Create a new </i><i>STDIN_NOT_FOUND</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::CONNECTION_FAILED()
</dt><dd>Create a new </i><i>CONNECTION_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_MAXTIME()
</dt><dd>Create a new </i><i>INVALID_MAXTIME</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_COUNT()
</dt><dd>Create a new </i><i>INVALID_COUNT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::NULL_SPECIFICATION_TREE()
</dt><dd>Create a new </i><i>NULL_SPECIFICATION_TREE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::JM_FAILED_ALLOW_ATTACH()
</dt><dd>Create a new </i><i>JM_FAILED_ALLOW_ATTACH</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::JOB_EXECUTION_FAILED()
</dt><dd>Create a new </i><i>JOB_EXECUTION_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_PARADYN()
</dt><dd>Create a new </i><i>INVALID_PARADYN</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_JOBTYPE()
</dt><dd>Create a new </i><i>INVALID_JOBTYPE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_GRAM_MYJOB()
</dt><dd>Create a new </i><i>INVALID_GRAM_MYJOB</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::BAD_SCRIPT_ARG_FILE()
</dt><dd>Create a new </i><i>BAD_SCRIPT_ARG_FILE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::ARG_FILE_CREATION_FAILED()
</dt><dd>Create a new </i><i>ARG_FILE_CREATION_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_JOBSTATE()
</dt><dd>Create a new </i><i>INVALID_JOBSTATE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_SCRIPT_REPLY()
</dt><dd>Create a new </i><i>INVALID_SCRIPT_REPLY</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_SCRIPT_STATUS()
</dt><dd>Create a new </i><i>INVALID_SCRIPT_STATUS</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::JOBTYPE_NOT_SUPPORTED()
</dt><dd>Create a new </i><i>JOBTYPE_NOT_SUPPORTED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::UNIMPLEMENTED()
</dt><dd>Create a new </i><i>UNIMPLEMENTED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::TEMP_SCRIPT_FILE_FAILED()
</dt><dd>Create a new </i><i>TEMP_SCRIPT_FILE_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::USER_PROXY_NOT_FOUND()
</dt><dd>Create a new </i><i>USER_PROXY_NOT_FOUND</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::OPENING_USER_PROXY()
</dt><dd>Create a new </i><i>OPENING_USER_PROXY</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::JOB_CANCEL_FAILED()
</dt><dd>Create a new </i><i>JOB_CANCEL_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::MALLOC_FAILED()
</dt><dd>Create a new </i><i>MALLOC_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::DUCT_INIT_FAILED()
</dt><dd>Create a new </i><i>DUCT_INIT_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::DUCT_LSP_FAILED()
</dt><dd>Create a new </i><i>DUCT_LSP_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_HOST_COUNT()
</dt><dd>Create a new </i><i>INVALID_HOST_COUNT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::UNSUPPORTED_PARAMETER()
</dt><dd>Create a new </i><i>UNSUPPORTED_PARAMETER</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_QUEUE()
</dt><dd>Create a new </i><i>INVALID_QUEUE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_PROJECT()
</dt><dd>Create a new </i><i>INVALID_PROJECT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_EVALUATION_FAILED()
</dt><dd>Create a new </i><i>RSL_EVALUATION_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::BAD_RSL_ENVIRONMENT()
</dt><dd>Create a new </i><i>BAD_RSL_ENVIRONMENT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::DRYRUN()
</dt><dd>Create a new </i><i>DRYRUN</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::ZERO_LENGTH_RSL()
</dt><dd>Create a new </i><i>ZERO_LENGTH_RSL</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::STAGING_EXECUTABLE()
</dt><dd>Create a new </i><i>STAGING_EXECUTABLE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::STAGING_STDIN()
</dt><dd>Create a new </i><i>STAGING_STDIN</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_JOB_MANAGER_TYPE()
</dt><dd>Create a new </i><i>INVALID_JOB_MANAGER_TYPE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::BAD_ARGUMENTS()
</dt><dd>Create a new </i><i>BAD_ARGUMENTS</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::GATEKEEPER_MISCONFIGURED()
</dt><dd>Create a new </i><i>GATEKEEPER_MISCONFIGURED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::BAD_RSL()
</dt><dd>Create a new </i><i>BAD_RSL</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::VERSION_MISMATCH()
</dt><dd>Create a new </i><i>VERSION_MISMATCH</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_ARGUMENTS()
</dt><dd>Create a new </i><i>RSL_ARGUMENTS</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_COUNT()
</dt><dd>Create a new </i><i>RSL_COUNT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_DIRECTORY()
</dt><dd>Create a new </i><i>RSL_DIRECTORY</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_DRYRUN()
</dt><dd>Create a new </i><i>RSL_DRYRUN</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_ENVIRONMENT()
</dt><dd>Create a new </i><i>RSL_ENVIRONMENT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_EXECUTABLE()
</dt><dd>Create a new </i><i>RSL_EXECUTABLE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_HOST_COUNT()
</dt><dd>Create a new </i><i>RSL_HOST_COUNT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_JOBTYPE()
</dt><dd>Create a new </i><i>RSL_JOBTYPE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_MAXTIME()
</dt><dd>Create a new </i><i>RSL_MAXTIME</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_MYJOB()
</dt><dd>Create a new </i><i>RSL_MYJOB</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_PARADYN()
</dt><dd>Create a new </i><i>RSL_PARADYN</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_PROJECT()
</dt><dd>Create a new </i><i>RSL_PROJECT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_QUEUE()
</dt><dd>Create a new </i><i>RSL_QUEUE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_STDERR()
</dt><dd>Create a new </i><i>RSL_STDERR</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_STDIN()
</dt><dd>Create a new </i><i>RSL_STDIN</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_STDOUT()
</dt><dd>Create a new </i><i>RSL_STDOUT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::OPENING_JOBMANAGER_SCRIPT()
</dt><dd>Create a new </i><i>OPENING_JOBMANAGER_SCRIPT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::CREATING_PIPE()
</dt><dd>Create a new </i><i>CREATING_PIPE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::FCNTL_FAILED()
</dt><dd>Create a new </i><i>FCNTL_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::STDOUT_FILENAME_FAILED()
</dt><dd>Create a new </i><i>STDOUT_FILENAME_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::STDERR_FILENAME_FAILED()
</dt><dd>Create a new </i><i>STDERR_FILENAME_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::FORKING_EXECUTABLE()
</dt><dd>Create a new </i><i>FORKING_EXECUTABLE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::EXECUTABLE_PERMISSIONS()
</dt><dd>Create a new </i><i>EXECUTABLE_PERMISSIONS</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::OPENING_STDOUT()
</dt><dd>Create a new </i><i>OPENING_STDOUT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::OPENING_STDERR()
</dt><dd>Create a new </i><i>OPENING_STDERR</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::OPENING_CACHE_USER_PROXY()
</dt><dd>Create a new </i><i>OPENING_CACHE_USER_PROXY</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::OPENING_CACHE()
</dt><dd>Create a new </i><i>OPENING_CACHE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INSERTING_CLIENT_CONTACT()
</dt><dd>Create a new </i><i>INSERTING_CLIENT_CONTACT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::CLIENT_CONTACT_NOT_FOUND()
</dt><dd>Create a new </i><i>CLIENT_CONTACT_NOT_FOUND</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::CONTACTING_JOB_MANAGER()
</dt><dd>Create a new </i><i>CONTACTING_JOB_MANAGER</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_JOB_CONTACT()
</dt><dd>Create a new </i><i>INVALID_JOB_CONTACT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::UNDEFINED_EXE()
</dt><dd>Create a new </i><i>UNDEFINED_EXE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::CONDOR_ARCH()
</dt><dd>Create a new </i><i>CONDOR_ARCH</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::CONDOR_OS()
</dt><dd>Create a new </i><i>CONDOR_OS</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_MIN_MEMORY()
</dt><dd>Create a new </i><i>RSL_MIN_MEMORY</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_MAX_MEMORY()
</dt><dd>Create a new </i><i>RSL_MAX_MEMORY</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_MIN_MEMORY()
</dt><dd>Create a new </i><i>INVALID_MIN_MEMORY</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_MAX_MEMORY()
</dt><dd>Create a new </i><i>INVALID_MAX_MEMORY</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::HTTP_FRAME_FAILED()
</dt><dd>Create a new </i><i>HTTP_FRAME_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::HTTP_UNFRAME_FAILED()
</dt><dd>Create a new </i><i>HTTP_UNFRAME_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::HTTP_PACK_FAILED()
</dt><dd>Create a new </i><i>HTTP_PACK_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::HTTP_UNPACK_FAILED()
</dt><dd>Create a new </i><i>HTTP_UNPACK_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_JOB_QUERY()
</dt><dd>Create a new </i><i>INVALID_JOB_QUERY</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::SERVICE_NOT_FOUND()
</dt><dd>Create a new </i><i>SERVICE_NOT_FOUND</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::JOB_QUERY_DENIAL()
</dt><dd>Create a new </i><i>JOB_QUERY_DENIAL</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::CALLBACK_NOT_FOUND()
</dt><dd>Create a new </i><i>CALLBACK_NOT_FOUND</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::BAD_GATEKEEPER_CONTACT()
</dt><dd>Create a new </i><i>BAD_GATEKEEPER_CONTACT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::POE_NOT_FOUND()
</dt><dd>Create a new </i><i>POE_NOT_FOUND</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::MPIRUN_NOT_FOUND()
</dt><dd>Create a new </i><i>MPIRUN_NOT_FOUND</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_START_TIME()
</dt><dd>Create a new </i><i>RSL_START_TIME</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_RESERVATION_HANDLE()
</dt><dd>Create a new </i><i>RSL_RESERVATION_HANDLE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_MAX_WALL_TIME()
</dt><dd>Create a new </i><i>RSL_MAX_WALL_TIME</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_MAX_WALL_TIME()
</dt><dd>Create a new </i><i>INVALID_MAX_WALL_TIME</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_MAX_CPU_TIME()
</dt><dd>Create a new </i><i>RSL_MAX_CPU_TIME</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_MAX_CPU_TIME()
</dt><dd>Create a new </i><i>INVALID_MAX_CPU_TIME</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::JM_SCRIPT_NOT_FOUND()
</dt><dd>Create a new </i><i>JM_SCRIPT_NOT_FOUND</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::JM_SCRIPT_PERMISSIONS()
</dt><dd>Create a new </i><i>JM_SCRIPT_PERMISSIONS</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::SIGNALING_JOB()
</dt><dd>Create a new </i><i>SIGNALING_JOB</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::UNKNOWN_SIGNAL_TYPE()
</dt><dd>Create a new </i><i>UNKNOWN_SIGNAL_TYPE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::GETTING_JOBID()
</dt><dd>Create a new </i><i>GETTING_JOBID</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::WAITING_FOR_COMMIT()
</dt><dd>Create a new </i><i>WAITING_FOR_COMMIT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::COMMIT_TIMED_OUT()
</dt><dd>Create a new </i><i>COMMIT_TIMED_OUT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_SAVE_STATE()
</dt><dd>Create a new </i><i>RSL_SAVE_STATE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_RESTART()
</dt><dd>Create a new </i><i>RSL_RESTART</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_TWO_PHASE_COMMIT()
</dt><dd>Create a new </i><i>RSL_TWO_PHASE_COMMIT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_TWO_PHASE_COMMIT()
</dt><dd>Create a new </i><i>INVALID_TWO_PHASE_COMMIT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_STDOUT_POSITION()
</dt><dd>Create a new </i><i>RSL_STDOUT_POSITION</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_STDOUT_POSITION()
</dt><dd>Create a new </i><i>INVALID_STDOUT_POSITION</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_STDERR_POSITION()
</dt><dd>Create a new </i><i>RSL_STDERR_POSITION</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_STDERR_POSITION()
</dt><dd>Create a new </i><i>INVALID_STDERR_POSITION</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RESTART_FAILED()
</dt><dd>Create a new </i><i>RESTART_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::NO_STATE_FILE()
</dt><dd>Create a new </i><i>NO_STATE_FILE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::READING_STATE_FILE()
</dt><dd>Create a new </i><i>READING_STATE_FILE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::WRITING_STATE_FILE()
</dt><dd>Create a new </i><i>WRITING_STATE_FILE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::OLD_JM_ALIVE()
</dt><dd>Create a new </i><i>OLD_JM_ALIVE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::TTL_EXPIRED()
</dt><dd>Create a new </i><i>TTL_EXPIRED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::SUBMIT_UNKNOWN()
</dt><dd>Create a new </i><i>SUBMIT_UNKNOWN</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_REMOTE_IO_URL()
</dt><dd>Create a new </i><i>RSL_REMOTE_IO_URL</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::WRITING_REMOTE_IO_URL()
</dt><dd>Create a new </i><i>WRITING_REMOTE_IO_URL</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::STDIO_SIZE()
</dt><dd>Create a new </i><i>STDIO_SIZE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::JM_STOPPED()
</dt><dd>Create a new </i><i>JM_STOPPED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::USER_PROXY_EXPIRED()
</dt><dd>Create a new </i><i>USER_PROXY_EXPIRED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::JOB_UNSUBMITTED()
</dt><dd>Create a new </i><i>JOB_UNSUBMITTED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_COMMIT()
</dt><dd>Create a new </i><i>INVALID_COMMIT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_SCHEDULER_SPECIFIC()
</dt><dd>Create a new </i><i>RSL_SCHEDULER_SPECIFIC</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::STAGE_IN_FAILED()
</dt><dd>Create a new </i><i>STAGE_IN_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_SCRATCH()
</dt><dd>Create a new </i><i>INVALID_SCRATCH</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_CACHE()
</dt><dd>Create a new </i><i>RSL_CACHE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_SUBMIT_ATTRIBUTE()
</dt><dd>Create a new </i><i>INVALID_SUBMIT_ATTRIBUTE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_STDIO_UPDATE_ATTRIBUTE()
</dt><dd>Create a new </i><i>INVALID_STDIO_UPDATE_ATTRIBUTE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_RESTART_ATTRIBUTE()
</dt><dd>Create a new </i><i>INVALID_RESTART_ATTRIBUTE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_FILE_STAGE_IN()
</dt><dd>Create a new </i><i>RSL_FILE_STAGE_IN</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_FILE_STAGE_IN_SHARED()
</dt><dd>Create a new </i><i>RSL_FILE_STAGE_IN_SHARED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_FILE_STAGE_OUT()
</dt><dd>Create a new </i><i>RSL_FILE_STAGE_OUT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_GASS_CACHE()
</dt><dd>Create a new </i><i>RSL_GASS_CACHE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_FILE_CLEANUP()
</dt><dd>Create a new </i><i>RSL_FILE_CLEANUP</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_SCRATCH()
</dt><dd>Create a new </i><i>RSL_SCRATCH</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_SCHEDULER_SPECIFIC()
</dt><dd>Create a new </i><i>INVALID_SCHEDULER_SPECIFIC</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::UNDEFINED_ATTRIBUTE()
</dt><dd>Create a new </i><i>UNDEFINED_ATTRIBUTE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_CACHE()
</dt><dd>Create a new </i><i>INVALID_CACHE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_SAVE_STATE()
</dt><dd>Create a new </i><i>INVALID_SAVE_STATE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::OPENING_VALIDATION_FILE()
</dt><dd>Create a new </i><i>OPENING_VALIDATION_FILE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::READING_VALIDATION_FILE()
</dt><dd>Create a new </i><i>READING_VALIDATION_FILE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_PROXY_TIMEOUT()
</dt><dd>Create a new </i><i>RSL_PROXY_TIMEOUT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_PROXY_TIMEOUT()
</dt><dd>Create a new </i><i>INVALID_PROXY_TIMEOUT</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::STAGE_OUT_FAILED()
</dt><dd>Create a new </i><i>STAGE_OUT_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::JOB_CONTACT_NOT_FOUND()
</dt><dd>Create a new </i><i>JOB_CONTACT_NOT_FOUND</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::DELEGATION_FAILED()
</dt><dd>Create a new </i><i>DELEGATION_FAILED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::LOCKING_STATE_LOCK_FILE()
</dt><dd>Create a new </i><i>LOCKING_STATE_LOCK_FILE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_ATTR()
</dt><dd>Create a new </i><i>INVALID_ATTR</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::NULL_PARAMETER()
</dt><dd>Create a new </i><i>NULL_PARAMETER</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::STILL_STREAMING()
</dt><dd>Create a new </i><i>STILL_STREAMING</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::AUTHORIZATION_DENIED()
</dt><dd>Create a new </i><i>AUTHORIZATION_DENIED</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::AUTHORIZATION_SYSTEM_FAILURE()
</dt><dd>Create a new </i><i>AUTHORIZATION_SYSTEM_FAILURE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::AUTHORIZATION_DENIED_JOB_ID()
</dt><dd>Create a new </i><i>AUTHORIZATION_DENIED_JOB_ID</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::AUTHORIZATION_DENIED_EXECUTABLE()
</dt><dd>Create a new </i><i>AUTHORIZATION_DENIED_EXECUTABLE</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::RSL_USER_NAME()
</dt><dd>Create a new </i><i>RSL_USER_NAME</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::INVALID_USER_NAME()
</dt><dd>Create a new </i><i>INVALID_USER_NAME</i><i> </i><i>GRAM</i><i> error.
</dd><dt>$error</i> = <i>Globus::GRAM::Error::LAST()
</dt><dd>Create a new </i><i>LAST</i><i> </i><i>GRAM</i><i> error. 
</dd></dl>
 </i>
