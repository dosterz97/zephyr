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
            `controllerId` bigint(20) UNSIGNED NOT NULL,
            `firstName` varchar(50) NOT NULL,
            `lastName` varchar(50) NOT NULL,
            `privilege` set('BASIC','ADVANCED','ADMIN') NOT NULL DEFAULT 'BASIC',
            `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (`userId`)
        );

        -- --------------------------------------------------------

        --
        -- Table structure for table `adjustment`
        --

        CREATE TABLE `adjustment` (
            `controllerId` bigint(20) UNSIGNED NOT NULL,
            `state` tinyint(1) NOT NULL,
            `brightness` int(11) NOT NULL,
            `red` int(11) NOT NULL,
            `blue` int(11) NOT NULL,
            `green` int(11) NOT NULL,
            `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
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
        -- Table structure for table `light`
        --

        CREATE TABLE `light` (
            `controllerId` bigint(20) UNSIGNED NOT NULL,
            `state` tinyint(1) NOT NULL,
            `brightness` int(11) NOT NULL,
            `red` int(11) NOT NULL,
            `blue` int(11) NOT NULL,
            `green` int(11) NOT NULL,
            PRIMARY KEY (`controllerId`)
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

        INSERT INTO `account` (
        )

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
