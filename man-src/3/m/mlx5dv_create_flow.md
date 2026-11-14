---
title: "mlx5dv_create_flow(3)"
name: "mlx5dv_create_flow"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_create_flow/"
---

<h2 class="name">NAME</h2>
 

 

 mlx5dv_create_flow - creates a steering flow rule 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/mlx5dv.h&gt;
struct ibv_flow *
mlx5dv_create_flow(struct mlx5dv_flow_matcher *flow_matcher,
                   struct mlx5dv_flow_match_parameters *match_value,
                   size_t num_actions,
                   struct mlx5dv_flow_action_attr actions_attr[])
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 mlx5dv_create_flow() creates a steering flow rule with the ability to specify specific driver properties.

<h2>ARGUMENTS</h2>

 

 Please see <a HREF="/docs/linux/man/3-mlx5dv_create_flow_matcher/">mlx5dv_create_flow_matcher</a>(3) for flow_matcher and match_value.
<dl>
<dt>num_actions
<dd> Specifies how many actions are passed in actions_attr</dl>

<h3>actions_attr</h3>

<dl>
<dt>
<dd> <pre><code>
struct mlx5dv_flow_action_attr {
    enum mlx5dv_flow_action_type type;
    union {
        struct ibv_qp *qp;
        struct ibv_counters *counter;
        struct ibv_flow_action *action;
        uint32_t tag_value;
        struct mlx5dv_devx_obj *obj;
    };
};
</code></pre>
<dt>type
<dd> MLX5DV_FLOW_ACTION_DEST_IBV_QP The QP passed will receive the matched packets. MLX5DV_FLOW_ACTION_IBV_FLOW_ACTION The flow action to be applied. MLX5DV_FLOW_ACTION_TAG Flow tag to be provided in work completion. MLX5DV_FLOW_ACTION_DEST_DEVX The DEVX destination object for the matched packets. MLX5DV_FLOW_ACTION_COUNTERS_DEVX The DEVX counter object for the matched packets.
<dt>qp
<dd> QP passed, to be used with type MLX5DV_FLOW_ACTION_DEST_IBV_QP.
<dt>action
<dd> Flow action, to be used with type MLX5DV_FLOW_ACTION_IBV_FLOW_ACTION see <a HREF="/docs/linux/man/3-mlx5dv_create_flow_action_modify_header/">mlx5dv_create_flow_action_modify_header</a>(3) and <a HREF="/docs/linux/man/3-mlx5dv_create_flow_action_packet_reformat/">mlx5dv_create_flow_action_packet_reformat</a>(3).
<dt>tag_value
<dd> tag value to be passed in the work completion, to be used with type MLX5DV_FLOW_ACTION_TAG see <a HREF="/docs/linux/man/3-ibv_create_cq_ex/">ibv_create_cq_ex</a>(3).
<dt>obj
<dd> DEVX object, to be used with type MLX5DV_FLOW_ACTION_DEST_DEVX or by MLX5DV_FLOW_ACTION_COUNTERS_DEVX.</dl>

<h2>RETURN VALUE</h2>

 

 mlx5dv_create_flow returns a pointer to the created flow rule, on error NULL will be returned and errno will be set.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-mlx5dv_create_flow_action_modify_header/">mlx5dv_create_flow_action_modify_header</a>(3), <a HREF="/docs/linux/man/3-mlx5dv_create_flow_action_packet_reformat/">mlx5dv_create_flow_action_packet_reformat</a>(3), <a HREF="/docs/linux/man/3-mlx5dv_create_flow_matcher/">mlx5dv_create_flow_matcher</a>(3), <a HREF="/docs/linux/man/3-mlx5dv_create_qp/">mlx5dv_create_qp</a>(3), <a HREF="/docs/linux/man/3-ibv_create_qp_ex/">ibv_create_qp_ex</a>(3) <a HREF="/docs/linux/man/3-ibv_create_cq_ex/">ibv_create_cq_ex</a>(3) <a HREF="/docs/linux/man/3-ibv_create_counters/">ibv_create_counters</a>(3)

<h2>AUTHOR</h2>

 

 Mark Bloch &lt;marb [at] mellanox.com&gt; 

<h2>Index</h2>


