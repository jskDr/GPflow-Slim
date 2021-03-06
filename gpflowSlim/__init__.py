# Copyright 2016 alexggmatthews, James Hensman
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# flake8: noqa

from __future__ import absolute_import

from ._version import __version__
from ._settings import SETTINGS as settings

from . import misc
from . import transforms
from . import conditionals
from . import densities
from . import likelihoods
from . import kernels
from . import ekernels
from . import priors
from . import models
from . import features
from . import neural_kernel_network

from .decors import name_scope

from . import base

from .params import Parameter as Param
from . import kernel_kitchen_sink
from . import mean_functions
from . import kronecker
from .interpolation_np import GridInteprolation