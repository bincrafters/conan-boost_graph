from conans import ConanFile, tools, os

class BoostGraphConan(ConanFile):
    name = "Boost.Graph"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/graph"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "graph"
    requires =  "Boost.Algorithm/1.64.0@bincrafters/testing", \
                      "Boost.Any/1.64.0@bincrafters/testing", \
                      "Boost.Array/1.64.0@bincrafters/testing", \
                      "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Bind/1.64.0@bincrafters/testing", \
                      "Boost.Concept_Check/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Conversion/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Detail/1.64.0@bincrafters/testing", \
                      "Boost.Disjoint_Sets/1.64.0@bincrafters/testing", \
                      "Boost.Foreach/1.64.0@bincrafters/testing", \
                      "Boost.Function/1.64.0@bincrafters/testing", \
                      "Boost.Functional/1.64.0@bincrafters/testing", \
                      "Boost.Integer/1.64.0@bincrafters/testing", \
                      "Boost.Iterator/1.64.0@bincrafters/testing", \
                      "Boost.Lexical_Cast/1.64.0@bincrafters/testing", \
                      "Boost.Math/1.64.0@bincrafters/testing", \
                      "Boost.Move/1.64.0@bincrafters/testing", \
                      "Boost.Mpl/1.64.0@bincrafters/testing", \
                      "Boost.Multi_Index/1.64.0@bincrafters/testing", \
                      "Boost.Optional/1.64.0@bincrafters/testing", \
                      "Boost.Parameter/1.64.0@bincrafters/testing", \
                      "Boost.Preprocessor/1.64.0@bincrafters/testing", \
                      "Boost.Property_Tree/1.64.0@bincrafters/testing", \
                      "Boost.Random/1.64.0@bincrafters/testing", \
                      "Boost.Range/1.64.0@bincrafters/testing", \
                      "Boost.Serialization/1.64.0@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.64.0@bincrafters/testing", \
                      "Boost.Spirit/1.64.0@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.Test/1.64.0@bincrafters/testing", \
                      "Boost.Throw_Exception/1.64.0@bincrafters/testing", \
                      "Boost.Tti/1.64.0@bincrafters/testing", \
                      "Boost.Tuple/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing", \
                      "Boost.Typeof/1.64.0@bincrafters/testing", \
                      "Boost.Unordered/1.64.0@bincrafters/testing", \
                      "Boost.Utility/1.64.0@bincrafters/testing", \
                      "Boost.Xpressive/1.64.0@bincrafters/testing"

                      # "Boost.Graph_Parallel/1.64.0@bincrafters/testing", \  # This is a circular dependency , Needs discussion
                      # "Boost.Bimap/1.64.0@bincrafters/testing", \ # This is a circular dependency , Needs discussion
                      # "Boost.Property_Map/1.64.0@bincrafters/testing", \       This is a circular dependency , Needs discussion
                                            
                      #algorithm9 any6 array3 assert1 bimap14 bind3 concept_check5 config0 conversion5 core2 detail5 disjoint_sets14 foreach8 function5 functional5 graph_parallel14 integer3 iterator5 lexical_cast8 math8 move3 mpl5 multi_index12 optional5 parameter10 preprocessor0 property_map14 property_tree13 random9 range7 serialization11 smart_ptr4 spirit11 static_assert1 test10 throw_exception2 tti6 tuple4 type_traits3 typeof5 unordered8 utility5 xpressive9
                      
    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="", src=include_dir)

    def package_id(self):
        self.info.header_only()