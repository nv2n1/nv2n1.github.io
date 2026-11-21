---

title: "mlx5dv_devx_ind_tbl_query(3)"
name: "mlx5dv_devx_ind_tbl_query"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_devx_ind_tbl_query/"
---

mlx5dv_devx_qp_modify - Modifies a verbs QP via DEVX 

 mlx5dv_devx_qp_query - Queries a verbs QP via DEVX 

 mlx5dv_devx_cq_modify - Modifies a verbs CQ via DEVX 

 mlx5dv_devx_cq_query - Queries a verbs CQ via DEVX 

 mlx5dv_devx_srq_modify - Modifies a verbs SRQ via DEVX 

 mlx5dv_devx_srq_query - Queries a verbs SRQ via DEVX 

 mlx5dv_devx_wq_modify - Modifies a verbs WQ via DEVX 

 mlx5dv_devx_wq_query - Queries a verbs WQ via DEVX 

 mlx5dv_devx_ind_tbl_modify - Modifies a verbs indirection table via DEVX 

 mlx5dv_devx_ind_tbl_query - Queries a verbs indirection table via DEVX 

<h2>SYNOPSIS</h2>

<dl>
<dt>
</dt><dd> <pre><code>
#include &lt;infiniband/mlx5dv.h&gt;
int mlx5dv_devx_qp_modify(struct ibv_qp *qp, const void *in, size_t inlen,
                          void *out, size_t outlen);
int mlx5dv_devx_qp_query(struct ibv_qp *qp, const void *in, size_t inlen,
                         void *out, size_t outlen);
int mlx5dv_devx_cq_modify(struct ibv_cq *cq, const void *in, size_t inlen,
                          void *out, size_t outlen);
int mlx5dv_devx_cq_query(struct ibv_cq *cq, const void *in, size_t inlen,
                         void *out, size_t outlen);
int mlx5dv_devx_srq_modify(struct ibv_srq *srq, const void *in, size_t inlen,
                           void *out, size_t outlen);
int mlx5dv_devx_srq_query(struct ibv_srq *srq, const void *in, size_t inlen,
                          void *out, size_t outlen);
int mlx5dv_devx_wq_modify(struct ibv_wq *wq, const void *in, size_t inlen,
                          void *out, size_t outlen);
int mlx5dv_devx_wq_query(struct ibv_wq *wq, const void *in, size_t inlen,
                         void *out, size_t outlen);
int mlx5dv_devx_ind_tbl_modify(struct ibv_rwq_ind_table *ind_tbl,
                               const void *in, size_t inlen,
                               void *out, size_t outlen);
int mlx5dv_devx_ind_tbl_query(struct ibv_rwq_ind_table *ind_tbl,
                              const void *in, size_t inlen,
                              void *out, size_t outlen);
</code></pre></dd></dl>

<h2>DESCRIPTION</h2>

 

 Modify / query a verb object over the DEVX interface. 

 The DEVX API enables direct access from the user space area to the mlx5 device driver by using the KABI mechanism. The main purpose is to make the user space driver as independent as possible from the kernel so that future device functionality and commands can be activated with minimal to none kernel changes. 

 The above APIs enables modifying/querying a verb object via the DEVX interface. This enables interoperability between verbs and DEVX. As such an application can use the create method from verbs (e.g. ibv_create_qp) and modify and query the created object via DEVX (e.g. mlx5dv_devx_qp_modify).

<h2>ARGUMENTS</h2>

<dl>
<dt>qp/cq/wq/srq/ind_tbl
</dt><dd> The ibv_xxx object to issue the action on.
</dd><dt>in
</dt><dd> A buffer which contains the command's input data provided in a device specification format.
</dd><dt>inlen
</dt><dd> The size of in buffer in bytes.
</dd><dt>out
</dt><dd> A buffer which contains the command's output data according to the device specification format.
</dd><dt>outlen
</dt><dd> The size of out buffer in bytes.</dd></dl>

<h2>RETURN VALUE</h2>

 

 Upon success 0 is returned or the value of errno on a failure.

<h2>SEE ALSO</h2>

 

 mlx5dv_open_device, mlx5dv_devx_obj_create 

 #AUTHOR 

 Yishai Hadas &lt;yishaih [at] mellanox.com&gt;
