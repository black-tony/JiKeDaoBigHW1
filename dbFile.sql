CREATE DATABASE  IF NOT EXISTS `bighw1` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bighw1`;
-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: bighw1
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `danmakuinfo`
--

DROP TABLE IF EXISTS `danmakuinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `danmakuinfo` (
  `danmakuText` varchar(100) NOT NULL,
  `danmakuColor` varchar(10) NOT NULL,
  `danmakuSize` int unsigned NOT NULL,
  `danmakuPos` int unsigned NOT NULL,
  `danmakuTime` int unsigned NOT NULL,
  `danmakuUser` varchar(50) NOT NULL,
  `danmakuVideo` varchar(100) NOT NULL,
  `danmakuId` int unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`danmakuId`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `danmakuinfo`
--

LOCK TABLES `danmakuinfo` WRITE;
/*!40000 ALTER TABLE `danmakuinfo` DISABLE KEYS */;
INSERT INTO `danmakuinfo` VALUES ('hhhhh','#ffffff',1,0,22,'root','登 子 的 酒',14),('asdasd','#0f4fb8',1,0,80,'root','登 子 的 酒',15),('bottom','#2a7afa',1,1,159,'root','登 子 的 酒',16),('top','#2a7afa',1,2,226,'root','登 子 的 酒',17);
/*!40000 ALTER TABLE `danmakuinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usersinfo`
--

DROP TABLE IF EXISTS `usersinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usersinfo` (
  `userName` varchar(50) NOT NULL,
  `userPswd` varchar(50) NOT NULL,
  `userRank` int unsigned NOT NULL,
  `userMail` varchar(50) NOT NULL,
  `userId` int unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`userId`,`userName`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usersinfo`
--

LOCK TABLES `usersinfo` WRITE;
/*!40000 ALTER TABLE `usersinfo` DISABLE KEYS */;
INSERT INTO `usersinfo` VALUES ('admin','admin',99,'null@null.com',1),('user1','user1',1,'null@null.com',2),('root','root',100,'null@null.com',3),('user2','user2',1,'asd',6);
/*!40000 ALTER TABLE `usersinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `videoinfo`
--

DROP TABLE IF EXISTS `videoinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `videoinfo` (
  `videoUrl` varchar(100) NOT NULL,
  `videoGraph` varchar(100) NOT NULL,
  `videoName` varchar(100) NOT NULL,
  `videoCate` varchar(100) NOT NULL,
  PRIMARY KEY (`videoUrl`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `videoinfo`
--

LOCK TABLES `videoinfo` WRITE;
/*!40000 ALTER TABLE `videoinfo` DISABLE KEYS */;
INSERT INTO `videoinfo` VALUES ('../static/videoInfo/video/animation/1.mp4','../static/videoInfo/graph/animation/1.webp','【原神PV】小恶魔胡桃的Happy Halloween！','animation'),('../static/videoInfo/video/animation/10.mp4','../static/videoInfo/graph/animation/10.webp','《明日方舟2》 过场动画泄露','animation'),('../static/videoInfo/video/animation/2.mp4','../static/videoInfo/graph/animation/2.webp','【第二集】女孩子怎么能打打杀杀啊！','animation'),('../static/videoInfo/video/animation/4.mp4','../static/videoInfo/graph/animation/4.webp','这，值得沸腾期待！','animation'),('../static/videoInfo/video/dance/1.mp4','../static/videoInfo/graph/dance/1.webp','我将抖肩舞、KFC猛男、金凯瑞摇头、鸡你太美、油田、骚虎融到了一个舞蹈里','dance'),('../static/videoInfo/video/dance/10.mp4','../static/videoInfo/graph/dance/10.webp','叫我一声 武大王嘉尔 过分吗（男粉在团委见面会上社死跳TITANIC）','dance'),('../static/videoInfo/video/dance/2.mp4','../static/videoInfo/graph/dance/2.webp','你的小新娘！！❤️ 大喜 ❤️【生日作】','dance'),('../static/videoInfo/video/dance/3.mp4','../static/videoInfo/graph/dance/3.webp','【菜菜】Happy Halloween','dance'),('../static/videoInfo/video/dance/5.mp4','../static/videoInfo/graph/dance/5.webp','新宿街头大跳英雄联盟主题曲','dance'),('../static/videoInfo/video/dance/6.mp4','../static/videoInfo/graph/dance/6.webp','四年前买的女仆装，我终于有机会穿了···【微小微】','dance'),('../static/videoInfo/video/dance/7.mp4','../static/videoInfo/graph/dance/7.webp','答应你们的，跳给全班同学看了！！！','dance'),('../static/videoInfo/video/dance/9.mp4','../static/videoInfo/graph/dance/9.webp','王嘉尔请你多跳舞，王嘉尔每次跳舞动作干净利落，swag又卡点，真的太喜欢这种观感了','dance'),('../static/videoInfo/video/life/4.mp4','../static/videoInfo/graph/life/4.webp','Gugalanna Park（复健一图流PV）','life'),('../static/videoInfo/video/life/8.mp4','../static/videoInfo/graph/life/8.webp','这些年的经历是如此难忘，这是一位粉丝剪辑，谢谢粉丝花时间制作','life'),('../static/videoInfo/video/movie/1.mp4','../static/videoInfo/graph/movie/1.webp','Netflix动画《英雄联盟:双城之战》终极预告，讲述金克丝+蔚两姐妹','movie'),('../static/videoInfo/video/movie/10.mp4','../static/videoInfo/graph/movie/10.webp','如果可以回到过去某个时刻，你想怎么做？','movie'),('../static/videoInfo/video/movie/2.mp4','../static/videoInfo/graph/movie/2.webp','网飞新剧《三体》章北海惹争议，还我英俊章北海！！','movie'),('../static/videoInfo/video/movie/3.mp4','../static/videoInfo/graph/movie/3.webp','【4K中字】《暗夜博士：莫比亚斯》首支官方预告片 索尼蜘蛛侠电影宇宙新片','movie'),('../static/videoInfo/video/movie/4.mp4','../static/videoInfo/graph/movie/4.webp','\"玩具总动员\"巴斯光年电影！皮克斯《光年正传》首曝预告','movie'),('../static/videoInfo/video/movie/5.mp4','../static/videoInfo/graph/movie/5.webp','【IGN】电影《巴斯光年》先导预告','movie'),('../static/videoInfo/video/movie/6.mp4','../static/videoInfo/graph/movie/6.webp','【丹尼尔·克雷格专访】演007最难的地方，是5点就要开工','movie'),('../static/videoInfo/video/movie/8.mp4','../static/videoInfo/graph/movie/8.webp','漫威电影《永恒族》官方十大主角能力介绍','movie'),('../static/videoInfo/video/movie/9.mp4','../static/videoInfo/graph/movie/9.webp','[中字]【不良少年与白手杖女孩】第五集预告（杉咲花 杉野遥亮）','movie'),('../static/videoInfo/video/music/1.mp4','../static/videoInfo/graph/music/1.webp','教科书演唱 曾一鸣 《三国恋》','music'),('../static/videoInfo/video/music/10.mp4','../static/videoInfo/graph/music/10.webp','【mothy_悪ノP】钢铁大小姐莉莉亚尔妮 【鏡音リン】','music'),('../static/videoInfo/video/music/5.mp4','../static/videoInfo/graph/music/5.webp','爸，游戏机到底是给咱俩谁买的？','music'),('../static/videoInfo/video/music/8.mp4','../static/videoInfo/graph/music/8.webp','登 子 的 酒','music'),('../static/videoInfo/video/music/9.mp4','../static/videoInfo/graph/music/9.webp','【VOCALOID x6】Ready Steady【Earthy X6】','music'),('../static/videoInfo/video/technology/1.mp4','../static/videoInfo/graph/technology/1.webp','【第一人称创意】 有魔法就是可以为所欲为','technology'),('../static/videoInfo/video/technology/3.mp4','../static/videoInfo/graph/technology/3.webp','双屏操作，一次坑7个队友！','technology'),('../static/videoInfo/video/technology/4.mp4','../static/videoInfo/graph/technology/4.webp','【诸神黄昏】如何永久告别流氓软件？全网最强流氓软件清除攻略！！！','technology'),('../static/videoInfo/video/technology/9.mp4','../static/videoInfo/graph/technology/9.webp','【吐血推荐】8款逆天实用的宝藏APP，错过就亏大了！','technology');
/*!40000 ALTER TABLE `videoinfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-07 19:06:44
