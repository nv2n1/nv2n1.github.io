---
title: "mlx4dv_init_obj(3)"
name: "mlx4dv_init_obj"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx4dv_init_obj/"
description: "mlx4dv_init_obj – Initialize mlx4 direct verbs object from ibv_xxx structures"
---

<h2 class="name">NAME</h2>
<p> mlx4dv_init_obj &#8211; Initialize mlx4 direct verbs object from ibv_xxx structures </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/mlx4dv.h&gt;
int mlx4dv_init_obj(struct mlx4dv_obj *obj, uint64_t obj_type);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>mlx4dv_init_obj()</code> This function will initialize mlx4dv_xxx structs based on supplied type. The information for initialization is taken from ibv_xx structs supplied as part of input. </p>
<p> Request information of CQ marks its owned by direct verbs for all consumer index related actions. The initialization type can be combination of several types together. </p>
<pre><code>
struct mlx4dv_qp {
    uint32_t *rdb;
    uint32_t *sdb;
    struct {
        uint32_t wqe_cnt;
        int wqe_shift;
        int offset;
    } sq;
    struct {
        uint32_t wqe_cnt;
        int wqe_shift;
        int offset;
    } rq;
    struct {
        void *buf;
        size_t length;
    } buf;
    uint64_t comp_mask;    /* Use enum mlx4dv_qp_comp_mask */
    off_t uar_mmap_offset; /* If MLX4DV_QP_MASK_UAR_MMAP_OFFSET is set in comp_mask, this will contain the mmap offset of *sdb* */
};
struct mlx4dv_cq {
    struct {
        void *buf;
        size_t length;
    } buf;
    uint32_t cqe_cnt;
    uint32_t cqn;
    uint32_t *set_ci_db;
    uint32_t *arm_db;
    int arm_sn;
    int cqe_size;
    uint64_t comp_mask; /* Use enum mlx4dv_cq_comp_mask */
    void *cq_uar;
};
struct mlx4dv_srq {
    struct {
        void *buf;
        size_t length;
    } buf;
    int wqe_shift;
    int head;
    int tail;
    uint32_t *db;
    uint64_t comp_mask;
};
struct mlx4dv_rwq {
    __be32 *rdb;
    struct {
        uint32_t wqe_cnt;
        int wqe_shift;
        int offset;
    } rq;
    struct {
        void *buf;
        size_t length;
    } buf;
    uint64_t comp_mask;
};
struct mlx4dv_obj {
    struct {
        struct ibv_qp *in;
        struct mlx4dv_qp *out;
    } qp;
    struct {
        struct ibv_cq *in;
        struct mlx4dv_cq *out;
    } cq;
};
enum mlx4dv_obj_type {
    MLX4DV_OBJ_QP = 1 &lt;&lt; 0,
    MLX4DV_OBJ_CQ = 1 &lt;&lt; 1,
    MLX4DV_OBJ_SRQ = 1 &lt;&lt; 2,
};
</code></pre>
<h2>RETURN VALUE</h2>
<p> 0 on success or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p>&nbsp;*&nbsp;Compatibility masks&nbsp;(comp_mask)&nbsp;are in/out fields.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-mlx4dv/">mlx4dv</a></code>(7)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Maor Gottlieb &lt;maorg [at] mellanox.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
