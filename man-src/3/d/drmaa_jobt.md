---
title: "drmaa_jobt(3)"
name: "drmaa_jobt"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmaa_jobt/"
---

<h2 class="name">NAME</h2>
 

 Job template operations. - 

 The function drmaa_allocate_job_template() SHALL allocate a new job template, returned in <i>jt</i>. The function drmaa_allocate_job_template() SHALL allocate a new job template, returned in <i>jt</i>. 

 The function drmaa_set_attribute() SHALL set the value of the scalar attribute, <i>name</i>, in the job template, <i>jt</i>, to the value, <i>value</i>. 

 The function drmaa_delete_job_template() SHALL free the job template pointed to by <i>jt</i>. 

 This template is used to describe the job to be submitted. This description is accomplished by setting the desired scalar and vector attributes to their appropriate values. This template is then used in the job submission process. 

<h2>Author</h2>

 

 Generated automatically by Doxygen for torque from the source code. 

<h2>Index</h2>


