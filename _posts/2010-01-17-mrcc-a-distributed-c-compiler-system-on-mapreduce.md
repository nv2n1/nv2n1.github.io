---
title: "mrcc \u2013 A Distributed C Compiler System on MapReduce (Archived 2010)"
date: 2010-01-17 07:18:29 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/mrcc-a-distributed-c-compiler-system-on-mapreduce/
---

> **Archived Content (2010):** This post describes a research project from 2010. The tools and versions mentioned (Hadoop 0.20, MapReduce Streaming) are historically significant but have been largely superseded by modern distributed build systems like Bazel Remote Execution and cloud-native CI/CD pipelines.


**Original Project Date:** January 2010

This post details the design and implementation of **mrcc**, an open-source compilation system that used MapReduce to distribute C code compilation across a cloud computing cluster. While the specific technologies have evolved, the core concept of distributed compilation remains a cornerstone of modern software engineering.

### Modern Context: Where are we in 2026?

In 2010, distributing compilation was a complex manual process involving Hadoop Streaming. Today, developers use tools like:

- **Bazel Remote Execution:** A standard for distributed builds used by Google, TikTok, and many others.
- **Buildbarn & Buildfarm:** Open-source implementations of the Remote Execution API.
- **Incredibuild & distcc:** Specialized tools for C/C++ distributed compilation that are much easier to set up than a Hadoop cluster.

Despite the age, the principles of parallelizing independent tasks (like compiling source files) across a network remain the same. Below is the original technical documentation for historical reference.

------------------------------------------------------------------------

The mrcc project’s homepage is here: **<a href="https://www.ericzma.com/projects/mrcc/" rel="nofollow noopener" target="_blank">mrcc project</a>**.

### Abstract

<a href="https://www.ericzma.com/projects/mrcc/" rel="nofollow noopener" target="_blank">mrcc</a> is an open source compilation system that uses MapReduce to distribute C code compilation across the servers of the cloud computing platform. mrcc is built to use Hadoop by default, but it is easy to port it to other could computing platforms, such as MRlite, by only changing the interface to the platform. The mrcc project homepage is <a href="https://www.ericzma.com/projects/mrcc/" rel="nofollow noopener" target="_blank">http://www.ericzma.com/projects/mrcc/</a> and the source code is public available.

### Introduction

Compiling a big project such as Linux may cost much time. Usually, a big project consists of many small source code files and many of these source files can be compiled simultaneously. Parallel compilation on distributed servers is a way to accelerate the compilation.

In this project, we build a compilation system on top of MapReduce for distributed compilation.

### Design and architecture

The system of mrcc consists of one master server that controls the job and many slave servers that do the compilation work as shown in Figure 1. The master and the slaves can be one of the jobtracker or the tasktracker of the MapReduce system.

<img src="https://www.systutorials.com/wp/files/2010/01/mrcc_f1.png" decoding="async" />

Figure 1: The architecture of mrcc

*mrcc* runs as a front end of *cc*. When compiling one project, the user only need to add *“-jN”* parameter and *“CC=mrcc”* at the end of the normal *“make”* arguments and make the project on the master server. make will build a dependency tree of the project source files and then fork multiple *mrcc* instances when several source files can be compiled in parallel.

*mrcc* will first do preprocessing such as expanding the options and inserting the header files into the source file. Then *mrcc* will determines whether the job can be done on MapReduce depending on the compiler’s options. For ensuring the correctness of the compilation, mrcc only distributes the jobs to slaves when they are safe. The other jobs are done on the master server locally.

When doing remote compilation, *mrcc* first put the preprocessed source file into the network file system which is HDFS when using Hadoop, then it runs the job on MapReduce. Only the mapper which is called *mrcc-map* is used in this system. *mrcc-map* first gets the source file from the network file system, and then it calls the compiler locally on the slave. After the compilation finished, *mrcc-map* puts the object file which is the result of the compilation back into the network file system. After *mrcc-map* finished, *mrcc* on the master server get the object file from network file system and puts it into the local file system on the master node. By now, the compilation of one source file is finished. *make* can go on to compile the other files that depends on the completed one.

### Implementation

The mrcc compilation system consists of two core parts: the main program *mrcc* and the mapper for MapReduce called *mrcc-map*.

The overall system consists of seven parts:

- The main program *mrcc* (mrcc.c, compile.c, remote.c, safeguard.c, exec.c);
- The mapper *mrcc-map* (mrcc-map.c);
- The compiler options processing part (args.c);
- The logging part (trace.c, traceenv.c);
- The network file system and MapReduce interface part (netfsutils.c, mrutils.c);
- The temporary files cleaning up part (tempfile.c, cleanup.c);
- Some other utilities for processing string, file path and name, and I/O operation (utils.c, files.c, io.c).

In this report, we only introduce the two core parts of this system: *mrcc* and *mrcc-map*.

#### mrcc

The work flow is shown as Figure 2. There are five time lines in the process: mrcc is called, begins to compile locally or remotely while source file is being preprocessed, the preprocessing finishes, mrcc returns and mrcc finishes. During this process one or two new process is created by mrcc for source preprocessing or compiling. And some other works such as logging are done which we will not introduce. In the work flow graph, only the core functions are shown.

<img src="https://www.systutorials.com/wp/files/2010/01/mrcc_f2.png" decoding="async" />

Figure 2: Work flow of mrcc

When mrcc is called, it first preprocesses the compiler options by functions such as *expand_preprocessor_options()* which expands the arguments passed to preprocessor. Then\* make_tmpnam()\* is called to creates a temporary file inside the temporary directory and registers it for later cleanup. In *make_tmpnam()* a random number is generated for the temporary file. We use this random number as the id of the job and the object file name. The temporary output directory of the MapReduce job will be generated from this id to avoid name conflict ion. For example, if the temporary file name for storing a preprocessed source file is “/tmp/mrcc_36994a30.i”, the object file name and the output directory name are “/tmp/mrcc_36994a30.o” and “/tmp/mrcc_36994a30.odir” on the network file system.

mrcc then scans the options to determine whether this job can be done on remote server by calling scan_args*()*. While scanning the arguments, mrcc should also determine the default output file name according to the input source name. It is a little hard because the cc option rules are pretty complex. After that, mrcc calls the *cpp_maybe()* function to fork another process to run the preprocessor. The preprocessor insert header files into the source file. So the compiler version on the master and slaves needn’t to be identical since the remote server needn’t to do preprocessing.

Then *mrcc* compiles the source remotely or locally depending on the compiler options. Local compilation is straight forward. mrcc wait for the preprocessor process to complete and fork another process to do the compilation.

If the source file can be compiled on remote server, mrcc calls the function *compile_remote()*. mrcc should first wait for preprocessor to complete. Then mrcc put the preprocessed file into the network file system. After that, mrcc calls *call_mapper()* to generate relevant options and arguments from the id of the temporary file and the options and arguments of the compiler. The it runs the job on MapReduce. In this project, we use Hadoop Streaming to run the mrcc-map on the slaves. The options for mrcc-map are passed with the streaming job options.

After mrcc-map successfully finishes the job, the object file now exists on the network file system. mrcc generates the output file name from the id of the temporary file and calls *get_result_fs()* to retrieve the object file from the network file system.

As soon as mrcc gets the object file, it returns so that *make* can continue to compile other source files that may depend on the completed one. But there are still several temporary files and directories on the network file system and local disk that needed to be cleaned up. We use a tricky function *atexit()* to do the cleaning up work after mrcc returns. By using *atexit()* some of the clean up I/O operation are done while the next compilation is running to improve the overall performance.

#### mrcc-map

mrcc-map is put in local directories on all the slaves servers. We doing this to avoid distributing the mrcc-map when the job is called because the mrcc-map does not changed during compiling one project. The flow of mrcc-map is simpler than mrcc as shown in Figure 3.

mrcc-map first parse it’s arguments and finds out the file id generated by mrcc and the compilation options and arguments. Then mrcc-map gets the preprocessed file from net file system according to the id. After getting the preprocessed file, mrcc-map calls the local gcc/cc compiler and passes the compilation options and arguments to it. Then mrcc-map puts the object file to the netwrok file system and returns immediately. The clean up work is done after mrcc-map finishes to parallel I/O operation and the compilation in the same way that mrcc does.

<img src="https://www.systutorials.com/wp/files/2010/01/mrcc_f31.png" decoding="async" />

Figure 3: mrcc-map work flow

### Evaluation

Please refer to this paper for the evaluation experiments and results:

**Z. Ma** and L. Gu.*The Limitation of MapReduce: A Probing Case and a Lightweight Solution*. In Proc. of the 1st Intl. Conf. on Cloud Computing, GRIDs, and Virtualization (CLOUD COMPUTING 2010). Nov. 21-26, 2010, Lisbon, Portugal. (<a href="https://www.ericzma.com/homepage/publication/ma2010mrlite.pdf" rel="nofollow noopener" target="_blank">PDF</a> from one author’s homepage)

### Installation and configuration

#### Install hadoop

Install Hadoop into a directory, such as /lhome/zma/hadoop and start Hadoop.

Please refer to this tutorial for how to install and start Hadoop:

#### Configuration

**In netfsutils.c:**

As an example, we assume hadoop command’s full path is: /lhome/zma/hadoop/bin/hadoop

Set the variables as follows (We use the full path to avoid bad PATH environment).

const char\* put_file_fs_cmd = "/lhome/zma/hadoop/bin/hadoop dfs -put";\
const char\* get_file_fs_cmd = "/lhome/zma/hadoop/bin/hadoop dfs -get";\
const char\* del_file_fs_cmd = "/lhome/zma/hadoop/bin/hadoop dfs -rm";\
const char\* del_dir_fs_cmd = "/lhome/zma/hadoop/bin/hadoop dfs -rmr";

**In mrutils.c**

Set the variables and We also use the full path.

const char\* mr_exec_cmd_prefix = "/lhome/zma/hadoop/bin/hadoop jar /lhome/zma/hadoop/contrib/streaming/hadoop-0.20.2-streaming.jar -mapper ";\
const char\* mr_exec_cmd_mapper = "/home/zma/bin/mrcc-map ";\
const char\* mr_exec_cmd_parameter = "-numReduceTasks 0 -input null -output ";\

#### Compile and install:

    $ make
    # make install

### How to use it

#### Compile the project using mrcc on MapReduce

As building a project:

\$ make -j16 CC=mrcc\

-jN: N is the maximum parallel compilation number. N may be set to the number of CPUs in the cluster.

#### Enable detailed logging if needed

On master node in the same shell where mrcc runs:

\$ . docs/mrcc.export\

Or set environment variables:

MRCC_LOG=./mrcc.log\
MRCC_VERBOSE=1\
export MRCC_LOG\
export MRCC_VERBOSE\

### Related work

GNU make can execute many commands simultaneously by using “-j” option. But make can only execute many commands on local machine. mrcc makes use of this feature of make and distributed these commands (compilation) across servers on MapReduce.

distcc is a program to distribute compilation of C/C++/Objective code between several machines on a network. distcc must use a daemon on every slaves and the master must controls all the jobs details such as load balance and failure tolerance. distcc is easy to set up and fast in a cluster with a small amount of machines, but it will be hard to manage this system when distcc is running on a computing platform with thousands of machines.

### References

- Dean, J. and Ghemawat, S. 2004. MapReduce: simplified data processing on large clusters. In Proceedings of the 6th Conference on Symposium on Operating Systems Design & Implementation – Volume 6 (San Francisco, CA, December 06 – 08, 2004).
- Hadoop project. <a href="http://hadoop.apache.org" rel="nofollow noopener" target="_blank">http://hadoop.apache.org</a>
- mrcc project. <a href="https://www.ericzma.com/projects/mrcc/" rel="nofollow noopener" target="_blank">http://www.ericzma.com/projects/mrcc/</a>
- Hadoop 0.20.1. <a href="https://hadoop.apache.org/releases.html" rel="nofollow noopener" target="_blank">http://hadoop.apache.org/common/releases.html#Download</a>
- Linux. <a href="http://www.kernel.org/" rel="nofollow noopener" target="_blank">http://www.kernel.org/</a>
- distcc project. <a href="https://github.com/distcc/distcc" rel="nofollow noopener" target="_blank">https://github.com/distcc/distcc</a>
- GNU make. <a href="http://www.gnu.org/software/make/" rel="nofollow noopener" target="_blank">http://www.gnu.org/software/make/</a>
- Zhiqiang Ma and Lin Gu.*The Limitation of MapReduce: A Probing Case and a Lightweight Solution*. In Proc. of the 1st Intl. Conf. on Cloud Computing, GRIDs, and Virtualization (CLOUD COMPUTING 2010). Nov. 21-26, 2010, Lisbon, Portugal.
