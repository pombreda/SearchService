# -*- coding: utf8 -*-
#
# Hound: Search service
# Copyright (C) 2012  GSyC/LibreSoft
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Felipe Ortega <jfelipe@libresoft.es>
#          Santiago Dueñas <sduenas@libresoft.es>

from entity import Entity
from function import Function

class Module(Entity):
    
    def __init__(self, name, start_line, end_line):
        self.__name = name
        self.__start_line = start_line
        self.__end_line = end_line    
        self.__functions = []
        
    def get_name(self):
        return self.__name
        
    def get_start_line(self):
        return self.__start_line
        
    def get_end_line(self):
        return self.__end_line
        
    def get_functions(self):
        return self.__functions
        
    def add_function(self, value):
        self.__functions.append(value)