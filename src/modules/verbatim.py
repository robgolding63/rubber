# This file is part of Rubber and thus covered by the GPL
# (c) Emmanuel Beffara, 2003
"""
Dependency analysis for package 'verbatim' in Rubber.
"""

from os.path import basename
import rubber
from rubber.util import *

class Module (rubber.Module):
	def __init__ (self, env, dict):
		self.env = env
		env.add_hook("verbatiminput", self.input)

	def input (self, dict):
		if not dict["arg"]:
			return 0
		file = dict["arg"]
		self.env.depends[file] = DependLeaf([file])
