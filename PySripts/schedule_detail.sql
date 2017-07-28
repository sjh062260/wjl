CREATE TABLE `schedule_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `biz_id` varchar(128) DEFAULT NULL COMMENT '业务ID（（广场ID，优惠券ID）……）',
  `job_code` int(11) DEFAULT NULL COMMENT '任务执行逻辑的code（JobEnum:优惠券上架……）',
  `trigger_time` datetime DEFAULT NULL COMMENT '触发时间（优惠券上架时间……）',
  `suc_flag` int(11) DEFAULT NULL COMMENT '任务执行成功标示 0 未执行 1执行中（队列中） 2成功 3 失败',
  `fail_reason` varchar(152) DEFAULT NULL COMMENT '失败原因',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT NULL,
  `description` varchar(128) DEFAULT NULL COMMENT '描述',
  PRIMARY KEY (`id`),
  KEY `idx_schedule_detail_suc_flag` (`suc_flag`) USING BTREE,
  KEY `idx_schedule_detail_trigger_time` (`trigger_time`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=65521 DEFAULT CHARSET=utf8mb4;