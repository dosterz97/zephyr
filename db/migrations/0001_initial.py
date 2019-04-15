from django.db import migrations

class Migration(migrations.Migration)
initial = True

dependencies = []

operations = [
    migrations.RunSQL(
        sql="""
        --
        -- Table structure for table `account`
        --

        CREATE TABLE `account` (
            `userId` bigint(20) UNSIGNED NOT NULL,
            `firstName` varchar(50) NOT NULL,
            `lastName` varchar(50) NOT NULL,
            `privilege` set('BASIC','ADVANCED','ADMIN') NOT NULL DEFAULT 'BASIC',
            `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (`userId`)
        );

        -- --------------------------------------------------------

        --
        -- Table structure for table `controller`
        --

        CREATE TABLE `controller` (
            `controllerId` bigint(20) UNSIGNED NOT NULL,
            `location` varchar(50) NOT NULL,
            `privilege` set('BASIC','ADVANCED','ADMIN') NOT NULL DEFAULT 'BASIC',
            `state` tinyint(1) NOT NULL,
            `brightness` int(11) NOT NULL,
            `color` BINARY(3) NOT NULL DEFAULT 'NULL',
            PRIMARY KEY (`controllerId`)
        );

        -- --------------------------------------------------------

        --
        -- Table structure for table `camera`
        --

        CREATE TABLE `camera` (
            `cameraId` bigint(20) UNSIGNED NOT NULL,
            `sensorId` bigint(20) UNSIGNED NOT NULL,
            `photoStorage` varchar(50) NOT NULL,
            `recording` tinyint(1) NOT NULL,
            PRIMARY KEY (`cameraId`)

        );

        -- --------------------------------------------------------

        --
        -- Table structure for table `frontdoor`
        --

        CREATE TABLE `frontdoor` (
            `status` tinyint(1) NOT NULL,
            `cameraId` bigint(20) UNSIGNED NOT NULL,
            PRIMARY KEY (`status`)
        );

        -- --------------------------------------------------------

        --
        -- Table structure for table `photo`
        --

        CREATE TABLE `photo` (
            `photoId` bigint(20) UNSIGNED NOT NULL,
            `photoStorage` int(11) NOT NULL,
            `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (`photoId`)
        );

        -- --------------------------------------------------------

        --
        -- Table structure for table `restriction`
        --

        CREATE TABLE `restriction` (
            `restrictionId` bigint(20) UNSIGNED NOT NULL,
            `deviceId` bigint(20) UNSIGNED NOT NULL,
            `userId` bigint(20) NOT NULL,
            `dayOfWeek` set('MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY') NOT NULL,
            `start` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
            `end` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
            `ratingRestriction` set('0','1','2','3') NOT NULL DEFAULT '0',
            PRIMARY KEY (`restrictionId`)
        );

        -- --------------------------------------------------------

        --
        -- Table structure for table `television`
        --

        CREATE TABLE `television` (
            `deviceId` bigint(20) UNSIGNED NOT NULL,
            `name` varchar(50) NOT NULL,
            PRIMARY KEY (`deviceId`)
        );

        -- --------------------------------------------------------

        --
        -- Table structure for table `televisionshow`
        --

        CREATE TABLE `televisionshow` (
            `showName` varchar(50) NOT NULL,
            `start` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
            `end` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
            `ratingRestriction` set('0','1','2','3') NOT NULL DEFAULT '0',
            PRIMARY KEY (`showName`)
        );

        -- --------------------------------------------------------

        --
        -- Dummy Data
        --

        -- Accounts

        INSERT INTO `account` (
            `userId`, `firstName`, `lastName`, `privilege`, `created`)
        VALUES (
            '123456789', 'Joe', 'Smith', 'ADMIN', '2019-04-10 15:15:31');

        INSERT INTO `account` (
            `userId`, `firstName`, `lastName`, `privilege`, `created`)
        VALUES (
            '987654321', 'Chip', 'Smith', 'BASIC', '2019-04-14 14:37:12');

        INSERT INTO `account` (
            `userId`, `firstName`, `lastName`, `privilege`, `created`)
        VALUES (
            '12344321', 'Chucky', 'Smith', 'BASIC', '2019-04-14 14:23:48');

        INSERT INTO `account` ( 
            `userId`, `firstName`, `lastName`, `privilege`, `created`)
        VALUES ( 
            '43211234', 'Jane', 'Smith', 'ADVANCED', '2019-04-10 15:37:24');

        INSERT INTO `account` (
            `userId`, `firstName`, `lastName`, `privilege`, `created`)
        VALUES (
            '19451945', 'Agitha', 'Smith', 'BASIC', '2019-04-14 13:45:33');


        -- Front Door

        INSERT INTO `frontdoor` (
            `status`, `cameraId`)
        VALUES (
            '0', '456456456');

        INSERT INTO `camera` (
            `cameraId`, `sensorId`, `photoStorage`, `recording`)
        VALUES (
            '456456456', '654654654', '/photos/visitors', '0');

        INSERT INTO `photo` (
            `photoId`, `photoStorage`, `created`)
        VALUES (
            '879456123', '/photos/visitors', '2019-04-11 12:32:11');

        -- Television

        INSERT INTO `television` (
            `deviveId`, `name`)
        VALUES (
            '888555222', 'Living Room');

        INSERT INTO `television` (
            `deviceId`, `name`)
        VALUES ( 
            '777444111', 'Kitchen');

        INSERT INTO `televisionshow` (
            `showName`, `start`, `end`, `ratingRestriction`)
        VALUES(
            'The Office', '2019-04-14 13:10:34', '2019-04-14 16:32;11', 1);

        INSERT INTO `televisionshow` (
            `showName`, `start`, `end`, `ratingRestriction`)
        VALUES (
            'SpongeBob', '2019-04-15 08:24:33', '2019-04-15 09:13:22', 0);

        INSERT INTO `televisionshow` (
            `showName`, `start`, `end`, `ratingRestriction`)
        VALUES ( 
            'Game Of Thrones', '2019-04-14 20:12:44', '2019-04-14 22:12:32', 3);

        INSERT INTO `restriction` ( 
            `restrictionId`, `deviceId`, `userId`, `dayOfWeek`, `start`, `end`, `ratingRestriction`)
        VALUES (
            '555555555', '888555222', '987654321', 'Friday', '05:00:00', '09:00:00', 1);

        INSERT INTO `restriction` (
            `restrictionId`, `deviceId`, `userId`, `dayOfWeek`, `start`, `end`, `ratingRestriction`)
        VALUES (
            '444444444', '888555222', '12344321', 'Friday', '04:00:00', '09:00:00', 1);

        -- Lights

        INSERT INTO `controller` (
            `controllerId`, `location`, `privilege`, `state`, `brightness`)
        VALUES (
            '777555333', 'living Room', 'ADVANCED', '1', '100');

        INSERT INTO `controller` (
            `controllerId`, `location`, `privilege`, `state`, `brightness`, `color`)
        VALUES (
            '999555111', 'Master Bedroom', 'ADVACED', '1', '75', UNHEX('ff0000'));

        INSERT INTO `controller` (
            `controllerId`, `location`, `privilege`, `state`, `brightness`, `color`)
        VALUES (
            '777555111', 'Chip's Room', 'BASIC', '0', '100', UNHEX('003aff'));

      """,
        reverse_sql="""
        DROP TABLE `account`;
        DROP TABLE `adjustment`;
        DROP TABLE `camera`;
        DROP TABLE `frontdoor`;
        DROP TABLE `light`;
        DROP TABLE `photo`;
        DROP TABLE `restriction`;
        DROP TABLE `television`;
        DROP TABLE `televisionshow`;
      """
    )
]
