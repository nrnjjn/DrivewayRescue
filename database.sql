/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - breakdownassist
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`breakdownassist` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `breakdownassist`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add login',7,'add_login'),
(26,'Can change login',7,'change_login'),
(27,'Can delete login',7,'delete_login'),
(28,'Can view login',7,'view_login'),
(29,'Can add mechanic',8,'add_mechanic'),
(30,'Can change mechanic',8,'change_mechanic'),
(31,'Can delete mechanic',8,'delete_mechanic'),
(32,'Can view mechanic',8,'view_mechanic'),
(33,'Can add petrol_pump',9,'add_petrol_pump'),
(34,'Can change petrol_pump',9,'change_petrol_pump'),
(35,'Can delete petrol_pump',9,'delete_petrol_pump'),
(36,'Can view petrol_pump',9,'view_petrol_pump'),
(37,'Can add service_center',10,'add_service_center'),
(38,'Can change service_center',10,'change_service_center'),
(39,'Can delete service_center',10,'delete_service_center'),
(40,'Can view service_center',10,'view_service_center'),
(41,'Can add tow_service',11,'add_tow_service'),
(42,'Can change tow_service',11,'change_tow_service'),
(43,'Can delete tow_service',11,'delete_tow_service'),
(44,'Can view tow_service',11,'view_tow_service'),
(45,'Can add user',12,'add_user'),
(46,'Can change user',12,'change_user'),
(47,'Can delete user',12,'delete_user'),
(48,'Can view user',12,'view_user'),
(49,'Can add request',13,'add_request'),
(50,'Can change request',13,'change_request'),
(51,'Can delete request',13,'delete_request'),
(52,'Can view request',13,'view_request'),
(53,'Can add rating',14,'add_rating'),
(54,'Can change rating',14,'change_rating'),
(55,'Can delete rating',14,'delete_rating'),
(56,'Can view rating',14,'view_rating'),
(57,'Can add feedback',15,'add_feedback'),
(58,'Can change feedback',15,'change_feedback'),
(59,'Can delete feedback',15,'delete_feedback'),
(60,'Can view feedback',15,'view_feedback'),
(61,'Can add chat',16,'add_chat'),
(62,'Can change chat',16,'change_chat'),
(63,'Can delete chat',16,'delete_chat'),
(64,'Can view chat',16,'view_chat');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `breakdownassist_chat` */

DROP TABLE IF EXISTS `breakdownassist_chat`;

CREATE TABLE `breakdownassist_chat` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `message` varchar(100) NOT NULL,
  `FROM_id` bigint(20) NOT NULL,
  `TO_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BreakdownAssist_chat_FROM_id_d43f87b0_fk_Breakdown` (`FROM_id`),
  KEY `BreakdownAssist_chat_TO_id_9090e470_fk_BreakdownAssist_login_id` (`TO_id`),
  CONSTRAINT `BreakdownAssist_chat_TO_id_9090e470_fk_BreakdownAssist_login_id` FOREIGN KEY (`TO_id`) REFERENCES `breakdownassist_login` (`id`),
  CONSTRAINT `BreakdownAssist_chat_FROM_id_d43f87b0_fk_Breakdown` FOREIGN KEY (`FROM_id`) REFERENCES `breakdownassist_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `breakdownassist_chat` */

insert  into `breakdownassist_chat`(`id`,`date`,`message`,`FROM_id`,`TO_id`) values 
(1,'2023-11-19','Hey',3,1);

/*Table structure for table `breakdownassist_feedback` */

DROP TABLE IF EXISTS `breakdownassist_feedback`;

CREATE TABLE `breakdownassist_feedback` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `feedback` varchar(100) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BreakdownAssist_feed_USER_id_4d9bd0f5_fk_Breakdown` (`USER_id`),
  CONSTRAINT `BreakdownAssist_feed_USER_id_4d9bd0f5_fk_Breakdown` FOREIGN KEY (`USER_id`) REFERENCES `breakdownassist_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `breakdownassist_feedback` */

/*Table structure for table `breakdownassist_login` */

DROP TABLE IF EXISTS `breakdownassist_login`;

CREATE TABLE `breakdownassist_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Username` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `Type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `breakdownassist_login` */

insert  into `breakdownassist_login`(`id`,`Username`,`Password`,`Type`) values 
(1,'athul@gmail.com','Athul@123','User'),
(2,'admin@gmail.com','Admin@123','admin'),
(3,'mohan@gmail.com','Mohan@123','mechanic'),
(4,'kiran@gmail.com','Kiran@123','mechanic'),
(5,'avinashkrishanarchana@gmail.com','Avinash@123','User');

/*Table structure for table `breakdownassist_mechanic` */

DROP TABLE IF EXISTS `breakdownassist_mechanic`;

CREATE TABLE `breakdownassist_mechanic` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `mechanic_name` varchar(100) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `specialization` varchar(100) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `district` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` int(11) NOT NULL,
  `status` varchar(100) NOT NULL,
  `availability` varchar(100) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BreakdownAssist_mech_LOGIN_id_30f8b941_fk_Breakdown` (`LOGIN_id`),
  CONSTRAINT `BreakdownAssist_mech_LOGIN_id_30f8b941_fk_Breakdown` FOREIGN KEY (`LOGIN_id`) REFERENCES `breakdownassist_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `breakdownassist_mechanic` */

insert  into `breakdownassist_mechanic`(`id`,`mechanic_name`,`phone`,`email`,`specialization`,`gender`,`district`,`place`,`post`,`pin`,`status`,`availability`,`LOGIN_id`) values 
(1,'Mohan',6222345672,'mohan@gmail.com','Dodge specialist','Male','kozhikode','puthiyangadi','kozhikode',673018,'Approved','Available',3),
(2,'Kiran',8592967139,'kiran@gmail.com','cars','Male','kozhikode','medical college','mavoor',673008,'Approved','Available',4);

/*Table structure for table `breakdownassist_petrol_pump` */

DROP TABLE IF EXISTS `breakdownassist_petrol_pump`;

CREATE TABLE `breakdownassist_petrol_pump` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `pump_name` varchar(100) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `breakdownassist_petrol_pump` */

/*Table structure for table `breakdownassist_rating` */

DROP TABLE IF EXISTS `breakdownassist_rating`;

CREATE TABLE `breakdownassist_rating` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `rating` varchar(100) NOT NULL,
  `MECHANIC_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BreakdownAssist_rati_MECHANIC_id_1ee69708_fk_Breakdown` (`MECHANIC_id`),
  KEY `BreakdownAssist_rati_USER_id_f7adbaed_fk_Breakdown` (`USER_id`),
  CONSTRAINT `BreakdownAssist_rati_USER_id_f7adbaed_fk_Breakdown` FOREIGN KEY (`USER_id`) REFERENCES `breakdownassist_user` (`id`),
  CONSTRAINT `BreakdownAssist_rati_MECHANIC_id_1ee69708_fk_Breakdown` FOREIGN KEY (`MECHANIC_id`) REFERENCES `breakdownassist_mechanic` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `breakdownassist_rating` */

insert  into `breakdownassist_rating`(`id`,`date`,`rating`,`MECHANIC_id`,`USER_id`) values 
(1,'2023-11-19','4',1,1),
(2,'2023-11-19','2.5',1,1),
(4,'2023-11-19','1.5',1,1),
(5,'2023-11-19','5',1,1),
(6,'2023-11-19','5',2,2),
(7,'2023-11-19','5',1,2);

/*Table structure for table `breakdownassist_request` */

DROP TABLE IF EXISTS `breakdownassist_request`;

CREATE TABLE `breakdownassist_request` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `MECHANIC_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BreakdownAssist_requ_MECHANIC_id_9709e250_fk_Breakdown` (`MECHANIC_id`),
  KEY `BreakdownAssist_requ_USER_id_49d6a6ff_fk_Breakdown` (`USER_id`),
  CONSTRAINT `BreakdownAssist_requ_USER_id_49d6a6ff_fk_Breakdown` FOREIGN KEY (`USER_id`) REFERENCES `breakdownassist_user` (`id`),
  CONSTRAINT `BreakdownAssist_requ_MECHANIC_id_9709e250_fk_Breakdown` FOREIGN KEY (`MECHANIC_id`) REFERENCES `breakdownassist_mechanic` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `breakdownassist_request` */

insert  into `breakdownassist_request`(`id`,`date`,`status`,`MECHANIC_id`,`USER_id`) values 
(1,'2023-11-19','approved',1,1);

/*Table structure for table `breakdownassist_service_center` */

DROP TABLE IF EXISTS `breakdownassist_service_center`;

CREATE TABLE `breakdownassist_service_center` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `center_name` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `breakdownassist_service_center` */

/*Table structure for table `breakdownassist_tow_service` */

DROP TABLE IF EXISTS `breakdownassist_tow_service`;

CREATE TABLE `breakdownassist_tow_service` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `tow_name` varchar(100) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `breakdownassist_tow_service` */

/*Table structure for table `breakdownassist_user` */

DROP TABLE IF EXISTS `breakdownassist_user`;

CREATE TABLE `breakdownassist_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(100) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` int(11) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BreakdownAssist_user_LOGIN_id_00b0f6ef_fk_Breakdown` (`LOGIN_id`),
  CONSTRAINT `BreakdownAssist_user_LOGIN_id_00b0f6ef_fk_Breakdown` FOREIGN KEY (`LOGIN_id`) REFERENCES `breakdownassist_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `breakdownassist_user` */

insert  into `breakdownassist_user`(`id`,`user_name`,`phone`,`email`,`gender`,`district`,`place`,`post`,`pin`,`LOGIN_id`) values 
(1,'Athul',9946532902,'athul@gmail.com','Male','kozhikode','poovattuparamba','poovattuparamba',673008,1),
(2,'Avinash',6222345672,'avinashkrishanarchana@gmail.com','Male','kozhikode','peringolam','kunnamangalam',673008,5);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(16,'BreakdownAssist','chat'),
(15,'BreakdownAssist','feedback'),
(7,'BreakdownAssist','login'),
(8,'BreakdownAssist','mechanic'),
(9,'BreakdownAssist','petrol_pump'),
(14,'BreakdownAssist','rating'),
(13,'BreakdownAssist','request'),
(10,'BreakdownAssist','service_center'),
(11,'BreakdownAssist','tow_service'),
(12,'BreakdownAssist','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'BreakdownAssist','0001_initial','2023-11-19 07:01:50.403125'),
(2,'contenttypes','0001_initial','2023-11-19 07:01:50.453947'),
(3,'auth','0001_initial','2023-11-19 07:01:50.796551'),
(4,'admin','0001_initial','2023-11-19 07:01:50.892733'),
(5,'admin','0002_logentry_remove_auto_add','2023-11-19 07:01:50.909773'),
(6,'admin','0003_logentry_add_action_flag_choices','2023-11-19 07:01:50.926234'),
(7,'contenttypes','0002_remove_content_type_name','2023-11-19 07:01:51.027151'),
(8,'auth','0002_alter_permission_name_max_length','2023-11-19 07:01:51.069501'),
(9,'auth','0003_alter_user_email_max_length','2023-11-19 07:01:51.101680'),
(10,'auth','0004_alter_user_username_opts','2023-11-19 07:01:51.130107'),
(11,'auth','0005_alter_user_last_login_null','2023-11-19 07:01:51.178007'),
(12,'auth','0006_require_contenttypes_0002','2023-11-19 07:01:51.186824'),
(13,'auth','0007_alter_validators_add_error_messages','2023-11-19 07:01:51.199026'),
(14,'auth','0008_alter_user_username_max_length','2023-11-19 07:01:51.246829'),
(15,'auth','0009_alter_user_last_name_max_length','2023-11-19 07:01:51.292236'),
(16,'auth','0010_alter_group_name_max_length','2023-11-19 07:01:51.338198'),
(17,'auth','0011_update_proxy_permissions','2023-11-19 07:01:51.357148'),
(18,'auth','0012_alter_user_first_name_max_length','2023-11-19 07:01:51.401674'),
(19,'sessions','0001_initial','2023-11-19 07:01:51.450619');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('3zw7ec2nrpnlg3an771u4jl5j7xx10km','eyJsaWQiOiIiLCJ1c2VyaWQiOiIxIiwibmV3IjoiMSJ9:1r4eDP:zUfFEqBbPTB3oo5IkDX3tEk0wrrLJxmytOp_0tZ1Fds','2023-12-03 09:35:43.038900');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
