##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install castor
#
# You can edit this file again by typing:
#
#     spack edit castor
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Castor(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "http://www.castor-project.org/"
    url = "https://github.com/chengaoyu/CASTOR/archive/2.0.1.tar.gz"

    version('2.0.1', '2fc24c8bad59f9ded3704339c0446ea9')

    # FIXME: Add dependencies if required.
    depends_on('root')

    def cmake_args(self):
        args = ['-DCASToR_USE_CMAKE=ON',
                '-DCASTOR_CONFIG=/home/chengaoyu/tools/spack/var/spack/stage/castor-2.0.1/config',
                '-DCASToR_64bits=ON',
                '-DCASToR_ROOT=ON',
                '-DCASToR_BUILD_SAMPLE_UTILITIES=ON',
                '-DCASToR_BUILD_GATE_UTILITIES=ON']
        return args