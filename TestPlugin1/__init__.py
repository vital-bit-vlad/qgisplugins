# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TestPlugin1
                                 A QGIS plugin
 Test Plugin
                             -------------------
        begin                : 2017-11-01
        copyright            : (C) 2017 by vital-bit.com
        email                : vlad@vital-bit.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load TestPlugin1 class from file TestPlugin1.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .TestPlugin1 import TestPlugin1
    return TestPlugin1(iface)
