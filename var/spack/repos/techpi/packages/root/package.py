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

from spack import *
import sys


class Root(CMakePackage):
    """ROOT is a data analysis framework."""

    homepage = "https://root.cern.ch"
    url      = "https://root.cern.ch/download/root_v6.09.02.source.tar.gz"

    version('6.14.00', '3613c930589734531ac8995486d41af5')
    version('6.13.08', '0b33d8558662e9c67f5179c92ae40d6b')
    version('6.13.06', '3549d1c31d83e07e27c6361e5c86e70c')
    version('6.13.04', 'd57009331db9a481d85be6917e0f3493')
    version('6.13.02', 'a64428a9073f2a95bf7cff120982da15')
    version('6.12.06', 'bef6535a5d0cdf471b550da45a10f605')
    version('6.12.04', '8529b4c4e2befe8bdaa343a8e5d7534c')
    version('6.12.02', 'a46d67cf473f2137b5a3a9849f8170da')
    version('6.11.02', '95e5705e203a5e0e70be7849c915f732')
    version('6.10.08', '48f5044e9588d94fb2d79389e48e1d73')
    version('6.09.02', '4188dfeafb72df339a3d688fe92f57ec')
    version('6.08.06', 'bcf0be2df31a317d25694ad2736df268', preferred=True)
    version('6.06.08', '6ef0fe9bd9f88f3ce8890e3651142ee4')
    version('6.06.06', '4308449892210c8d36e36924261fea26')
    version('6.06.04', '55a2f98dd4cea79c9c4e32407c2d6d17')
    version('6.06.02', 'e9b8b86838f65b0a78d8d02c66c2ec55')
    version('5.34.36', '6a1ad549b3b79b10bbb1f116b49067ee')

    if sys.platform == 'darwin':
        patch('math_uint.patch', when='@6.06.02')
        patch('root6-60606-mathmore.patch', when='@6.06.06')

    variant('graphviz', default=False, description='Enable graphviz support')

    depends_on('cmake@3.4.3:', type='build')
    depends_on('pkgconfig',   type='build')

    depends_on('binutils')
    depends_on('zlib')
    # depends_on('unuran')
    depends_on('freetype')
    depends_on('pcre')
    depends_on('xz')
    depends_on('libsm')
    depends_on('libice')
    depends_on('libx11')
    depends_on('libxext')
    depends_on('libxpm')
    depends_on('libxft')
    # depends_on('gif')
    depends_on('libpng')
    depends_on('jpeg')
    depends_on('gsl')
    depends_on('python@2.7:')
    # depends_on('opengl')
    depends_on('graphviz', when='+graphviz')
    # depends_on('kerberos')
    depends_on('libxml2+python')
    depends_on('openssl')
    # depends_on('castor')
    # depends_on('rfio')
    # depends_on('mysql')
    # depends_on('oracle')
    # depends_on('odbc')
    # depends_on('postgresql')
    depends_on('sqlite')
    # depends_on('pythia')
    depends_on('fftw')
    depends_on('cfitsio')
    # depends_on('monalisa')
    # depends_on('xrootd')
    # depends_on('gfal')
    # depends_on('dcap')
    # depends_on('ldap')
    # depends_on('chirp')
    # depends_on('hdfs')
    # depends_on('davix')

    # I was unable to build root with any Intel compiler
    # See https://sft.its.cern.ch/jira/browse/ROOT-7517
    conflicts('%intel')

    def cmake_args(self):
        args = [
            '-Dcocoa=OFF',
            '-Dbonjour=OFF',
            '-Dx11=ON',
        ]

        if sys.platform == 'darwin':
            args.extend([
                '-Dcastor=OFF',
                '-Drfio=OFF',
                '-Ddcache=OFF',
            ])

        return args

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        spack_env.set('ROOTSYS', self.prefix)
        spack_env.set('ROOT_VERSION', 'v{0}'.format(self.version.up_to(1)))
        spack_env.prepend_path('PYTHONPATH', self.prefix.lib)
