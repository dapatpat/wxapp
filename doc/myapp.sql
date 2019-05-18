/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50726
Source Host           : localhost:3306
Source Database       : minipro

Target Server Type    : MYSQL
Target Server Version : 50726
File Encoding         : 65001

Date: 2019-05-15 12:19:36
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for myapp_pageconfig
-- ----------------------------
DROP TABLE IF EXISTS `myapp_pageconfig`;
CREATE TABLE `myapp_pageconfig` (
  `ConfigID` int(11) NOT NULL,
  `ConfigType` int(11) DEFAULT NULL,
  `ConfigTypeNmae` varchar(120) DEFAULT NULL,
  `ConfigKeyNo` int(11) DEFAULT NULL,
  `ConfigKeyName` varchar(120) DEFAULT NULL,
  `ConfigKeyValue` varchar(120) DEFAULT NULL,
  `ConfigFlag` tinyint(1) DEFAULT NULL,
  `ConfigCreatTime` date DEFAULT NULL,
  `ConfigDataType` int(11) DEFAULT NULL,
  PRIMARY KEY (`ConfigID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of myapp_pageconfig
-- ----------------------------
INSERT INTO `myapp_pageconfig` VALUES ('1', '1', 'IndexCol', '1', 'IndexColName', '热销', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('2', '1', 'IndexCol', '1', 'IndexColNameColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('3', '1', 'IndexCol', '1', 'IndexColBorderR', '50%', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('4', '1', 'IndexCol', '1', 'IndexColBackColor', '#ccc', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('5', '1', 'IndexCol', '1', 'IndexColBoxShadow', '#ddd', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('6', '1', 'IndexCol', '1', 'IndexColImgUrl', '', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('7', '1', 'IndexCol', '2', 'IndexColName', '促销', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('8', '1', 'IndexCol', '2', 'IndexColNameColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('9', '1', 'IndexCol', '2', 'IndexColBorderR', '50%', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('10', '1', 'IndexCol', '2', 'IndexColBackColor', '#ccc', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('11', '1', 'IndexCol', '2', 'IndexColBoxShadow', '#ddd', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('12', '1', 'IndexCol', '2', 'IndexColImgUrl', '', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('13', '1', 'IndexCol', '3', 'IndexColName', '优惠', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('14', '1', 'IndexCol', '3', 'IndexColNameColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('15', '1', 'IndexCol', '3', 'IndexColBorderR', '50%', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('16', '1', 'IndexCol', '3', 'IndexColBackColor', '#ccc', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('17', '1', 'IndexCol', '3', 'IndexColBoxShadow', '#ddd', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('18', '1', 'IndexCol', '3', 'IndexColImgUrl', '', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('19', '1', 'IndexCol', '4', 'IndexColName', '爆款', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('20', '1', 'IndexCol', '4', 'IndexColNameColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('21', '1', 'IndexCol', '4', 'IndexColBorderR', '50%', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('22', '1', 'IndexCol', '4', 'IndexColBackColor', '#ccc', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('23', '1', 'IndexCol', '4', 'IndexColBoxShadow', '#ddd', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('24', '1', 'IndexCol', '4', 'IndexColImgUrl', '', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('25', '2', 'IndexSwiperAreaTitle', '1', 'IndexSwiperAreaTitleName', '热销榜', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('26', '2', 'IndexSwiperAreaTitle', '1', 'IndexSwiperAreaTitleColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('27', '3', 'IndexSwiperAreaMore', '1', 'IndexSwiperAreaMoreName', '更多', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('28', '3', 'IndexSwiperAreaMore', '1', 'IndexSwiperAreaMoreColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('29', '3', 'IndexSwiperAreaMore', '1', 'IndexSwiperAreaMoreUrl', '', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('30', '4', 'IndexSwiperAreaGood', '1', 'IndexSwiperAreaGoodNameColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('31', '4', 'IndexSwiperAreaGood', '1', 'IndexSwiperAreaGoodBorderR', '50%', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('32', '4', 'IndexSwiperAreaGood', '1', 'IndexSwiperAreaGoodPriceColor', '', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('33', '5', 'IndexSplitLine', '1', 'IndexSplitLineHeight', '6px', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('34', '5', 'IndexSplitLine', '1', 'IndexSplitLineBackColor', '#ccc', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('35', '6', 'IndexListArea', '1', 'IndexListAreaTitleName', '商品列表', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('36', '6', 'IndexListArea', '1', 'IndexListAreaTitleColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('37', '7', 'IndexListAreaGood', '1', 'IndexListAreaGoodNameColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('38', '7', 'IndexListAreaGood', '1', 'IndexListAreaGoodIntroColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('39', '7', 'IndexListAreaGood', '1', 'IndexListAreaGoodNatureColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('40', '7', 'IndexListAreaGood', '1', 'IndexListAreaGoodPriceColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('41', '7', 'IndexListAreaGood', '1', 'IndexListAreaGoodLikeColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('42', '7', 'IndexListAreaGood', '1', 'IndexListAreaGoodBorderR', '50%', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('43', '7', 'SelectShop', '1', 'SelectShopNameColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('44', '7', 'SelectShop', '1', 'SelectShopIntroColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('45', '7', 'SelectShop', '1', 'SelectShopAddressColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('46', '7', 'SelectShop', '1', 'SelectShopTelColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('47', '7', 'SelectShop', '1', 'SelectShopBorderR', '50%', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('48', '8', 'SelectHorse', '1', 'SelectHorseUrl', '', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('49', '8', 'SelectHorse', '1', 'SelectHorseBackColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('50', '8', 'SelectHorse', '1', 'SelectHorseColor', '#ccc', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('51', '9', 'SelectCol', '1', 'SelectColName', '武侠', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('52', '9', 'SelectCol', '1', 'SelectColNameColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('53', '9', 'SelectCol', '1', 'SelectColBorderBottom', '1px', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('54', '9', 'SelectCol', '1', 'SelectColBorderLeft', '1px', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('55', '9', 'SelectCol', '1', 'SelectColBorderRight', '1px', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('56', '9', 'SelectCol', '1', 'SelectColBorderRightColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('57', '9', 'SelectCol', '1', 'SelectColBorderLeftColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('58', '9', 'SelectCol', '1', 'SelectColBorderBottomColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('59', '9', 'SelectCol', '1', 'SelectColBackColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('60', '9', 'SelectCol', '1', 'UnSelectColNameColor', '#ccc', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('61', '9', 'SelectCol', '1', 'UnSelectColBorderBottom', '0', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('62', '9', 'SelectCol', '1', 'UnSelectColBorderLeft', '0', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('63', '9', 'SelectCol', '1', 'UnSelectColBorderRight', '0', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('64', '9', 'SelectCol', '1', 'UnSelectColBorderRightColor', '#ccc', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('65', '9', 'SelectCol', '1', 'UnSelectColBorderLeftColor', '#ccc', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('66', '9', 'SelectCol', '1', 'UnSelectColBorderBottomColor', '#ccc', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('67', '9', 'SelectCol', '1', 'UnSelectColBackColor', '#ccc', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('68', '9', 'SelectCol', '2', 'SelectColName', '言情', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('69', '9', 'SelectCol', '2', 'SelectColNameColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('70', '9', 'SelectCol', '2', 'SelectColBorderBottom', '1px', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('71', '9', 'SelectCol', '2', 'SelectColBorderLeft', '1px', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('72', '9', 'SelectCol', '2', 'SelectColBorderRight', '1px', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('73', '9', 'SelectCol', '2', 'SelectColBorderRightColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('74', '9', 'SelectCol', '2', 'SelectColBorderLeftColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('75', '9', 'SelectCol', '2', 'SelectColBorderBottomColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('76', '9', 'SelectCol', '2', 'SelectColBackColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('77', '9', 'SelectCol', '2', 'UnSelectColNameColor', '#ccc', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('78', '9', 'SelectCol', '2', 'UnSelectColBorderBottom', '0', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('79', '9', 'SelectCol', '2', 'UnSelectColBorderLeft', '0', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('80', '9', 'SelectCol', '2', 'UnSelectColBorderRight', '0', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('81', '9', 'SelectCol', '2', 'UnSelectColBorderRightColor', '#ccc', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('82', '9', 'SelectCol', '2', 'UnSelectColBorderLeftColor', '#ccc', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('83', '9', 'SelectCol', '2', 'UnSelectColBorderBottomColor', '#ccc', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('84', '9', 'SelectCol', '2', 'UnSelectColBackColor', '#ccc', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('85', '10', 'SelectGood', '1', 'SelectGoodNameColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('86', '10', 'SelectGood', '1', 'SelectGoodIntroColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('87', '10', 'SelectGood', '1', 'SelectGoodTelColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('88', '10', 'SelectGood', '1', 'SelectGoodPriceColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('89', '10', 'SelectGood', '1', 'SelectGoodLikeColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('90', '10', 'SelectGood', '1', 'SelectGoodBorderR', '50%', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('91', '11', 'Article', '1', 'ArticleColName', '科幻', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('92', '11', 'Article', '1', 'ArticleColNameColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('93', '11', 'Article', '1', 'ArticleColBorderBottom', '1px', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('94', '11', 'Article', '1', 'ArticleColBorderBottomColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('95', '11', 'Article', '1', 'UnArticleColNameColor', '#333', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('96', '11', 'Article', '1', 'UnArticleColBorderBottom', '0', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('97', '11', 'Article', '1', 'UnArticleColBorderBottomColor', '', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('98', '11', 'Article', '2', 'ArticleColName', '文学', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('99', '11', 'Article', '2', 'ArticleColNameColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('100', '11', 'Article', '2', 'ArticleColBorderBottom', '1px', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('101', '11', 'Article', '2', 'ArticleColBorderBottomColor', '#red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('102', '11', 'Article', '2', 'UnArticleColNameColor', '#333', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('103', '11', 'Article', '2', 'UnArticleColBorderBottom', '0', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('104', '11', 'Article', '2', 'UnArticleColBorderBottomColor', '', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('105', '12', 'Article', '1', 'ArticleTitleNameCOlor', '#red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('106', '12', 'Article', '1', 'ArticleTitleIntroCOlor', '#red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('107', '12', 'Article', '1', 'ArticleTitleLikeCOlor', '#red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('108', '12', 'Article', '1', 'ArticleTitleTimeCOlor', '#red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('109', '13', 'Car', '1', 'CarCheckedUrl', '', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('110', '13', 'Car', '1', 'UnCarCheckedUrl', '', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('111', '13', 'Car', '1', 'CarGoodBorderR', '50%', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('112', '13', 'Car', '1', 'CarGoodNameColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('113', '13', 'Car', '1', 'CarGoodIntroColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('114', '13', 'Car', '1', 'CarGoodPriceColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('115', '13', 'Car', '1', 'CarGoodCountColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('116', '13', 'Car', '1', 'CarGoodStandardColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('117', '13', 'Car', '1', 'CarAllCheckedUrl', '', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('118', '13', 'Car', '1', 'CarAllCheckedBackColor', '#ccc', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('119', '13', 'Car', '1', 'CarAllCheckedColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('120', '14', 'MineInfo', '1', 'MineInfoBorderR', '50%', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('121', '14', 'MineInfo', '1', 'MineInfoNameColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('122', '14', 'MineInfo', '1', 'MineInfoSignColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('123', '14', 'MineInfo', '1', 'MineInfoBackColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('124', '14', 'MineInfo', '1', 'MineInfoBoxShadow', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('125', '15', 'MineOrder', '1', 'MineOrderNameColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('126', '15', 'MineOrder', '1', 'MineOrderAllOrderUrl', '', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('127', '15', 'MineOrder', '1', 'MineOrderAllOrderColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('128', '16', 'MineOrderStatus', '1', 'MineOrderStatusUrl', '', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('129', '16', 'MineOrderStatus', '1', 'MineOrderStatusName', '待发货', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('130', '16', 'MineOrderStatus', '1', 'MineOrderStatusNameColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('131', '16', 'MineOrderStatus', '2', 'MineOrderStatusUrl', '', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('132', '16', 'MineOrderStatus', '2', 'MineOrderStatusName', '已发货', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('133', '16', 'MineOrderStatus', '2', 'MineOrderStatusNameColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('134', '16', 'MineOrderStatus', '3', 'MineOrderStatusUrl', '', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('135', '16', 'MineOrderStatus', '3', 'MineOrderStatusName', '待收货', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('136', '16', 'MineOrderStatus', '3', 'MineOrderStatusNameColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('137', '16', 'MineOrderStatus', '4', 'MineOrderStatusUrl', '', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('138', '16', 'MineOrderStatus', '4', 'MineOrderStatusName', '已收货', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('139', '16', 'MineOrderStatus', '4', 'MineOrderStatusNameColor', 'red', '1', null, '1');
INSERT INTO `myapp_pageconfig` VALUES ('140', '17', 'MineGueset', '1', 'MineGuesetInfoUrl', '', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('141', '17', 'MineGueset', '1', 'MineGuesetInfoColor', '', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('142', '17', 'MineGueset', '1', 'MineGuesetAddressUrl', '', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('143', '17', 'MineGueset', '1', 'MineGuesetAddressColor', '', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('144', '17', 'MineGueset', '1', 'MineGuesetSplitLineColor', '#ccc', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('145', '17', 'MineGueset', '1', 'MineGuesetSplitLineHeight', '1px', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('146', '18', 'GDteialGood', '1', 'GDteialGoodNameColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('147', '18', 'GDteialGood', '1', 'GDteialGoodIntroColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('148', '18', 'GDteialGood', '1', 'GDteialGoodNatureColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('149', '18', 'GDteialGood', '1', 'GDteialGoodLikeColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('150', '18', 'GDteialGood', '1', 'GDteialGoodPriceColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('151', '18', 'GDteialGood', '1', 'GDteialGoodDetailColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('152', '18', 'GDteialGood', '1', 'GDteialGoodStandardColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('153', '18', 'GDteialGood', '1', 'GDteialGoodSayColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('154', '18', 'GDteialGood', '1', 'GDteialGoodDetailBorderColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('155', '18', 'GDteialGood', '1', 'GDteialGoodStandardBorderColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('156', '18', 'GDteialGood', '1', 'GDteialGoodSayBorderColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('157', '18', 'GDteialGood', '1', 'UnGDteialGoodDetailColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('158', '18', 'GDteialGood', '1', 'UnGDteialGoodStandardColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('159', '18', 'GDteialGood', '1', 'UnGDteialGoodSayColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('160', '18', 'GDteialGood', '1', 'UnGDteialGoodDetailBorderColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('161', '18', 'GDteialGood', '1', 'UnGDteialGoodStandardBorderColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('162', '18', 'GDteialGood', '1', 'UnGDteialGoodSayBorderColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('163', '19', 'SureButton', '1', 'SureButtonColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('164', '19', 'SureButton', '1', 'SureButtonBackColor', '#ccc', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('165', '19', 'SureButton', '1', 'SureButtonBorderColor', '#ccc', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('166', '20', 'CencelButton', '1', 'CencelButtonColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('167', '20', 'CencelButton', '1', 'CencelButtonBackColor', '#ccc', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('168', '20', 'CencelButton', '1', 'CencelButtonBorderColor', '#ccc', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('169', '21', 'DefaultButton', '1', 'DefaultButtonColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('170', '21', 'DefaultButton', '1', 'DefaultButtonBackColor', '#ccc', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('171', '21', 'DefaultButton', '1', 'DefaultButtonBorderColor', '#ccc', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('172', '22', 'OrderGood', '1', 'OrderGoodNameColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('173', '22', 'OrderGood', '1', 'OrderGoodIntroColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('174', '22', 'OrderGood', '1', 'OrderGoodPriceColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('175', '22', 'OrderGood', '1', 'OrderGoodNatureColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('176', '22', 'OrderGood', '1', 'OrderGoodCountColor', 'red', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('177', '22', 'OrderGood', '1', 'OrderGoodBorderR', '50%', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('178', '22', 'OrderGood', '1', 'OrderGoodCheckedUrl', '', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('179', '23', 'OrderChecked', '1', 'OrderCheckedBackColor', '#ccc', '1', null, '2');
INSERT INTO `myapp_pageconfig` VALUES ('180', '23', 'OrderChecked', '1', 'OrderCheckedColor', '#ccc', '1', null, '2');
