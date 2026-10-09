"""


:author: Quoc Bui, Eric Nicholson
:contact: Quoc Bui
:email: qvb2@cornell.edu
:organization: Cornell University School of Integrative Plant Science, Plant Biology Section
:address: 236 Mann Dr, Ithaca, NY 14853
:copyright: 
:date: Sep 16 2026 14:59
:dragonflyVersion: 2025.1.0.2063
:UUID: f661f1feb20011f192fd001a7dda7115
"""

__version__ = '1.0.11'

# Action log Wed Sep 16 15:01:02 2026

# Macro name: AI Segmentation by Merging Outputs Template Macro

# ********** BEGIN MACRO ********** #
"""
Invert the data of a dataset along specified axes.

:name: invert
:execution: execute

:param structuredGrid: the dataset to invert
:type structuredGrid: ORSModel.ors.StructuredGrid
:param invertX: if True, the X axis will be inverted
:type invertX: bool
:param invertY: if True, the Y axis will be inverted
:type invertY: bool
:param invertZ: if True, the Z axis will be inverted
:type invertZ: bool
:param invertData: if True, the data will be inverted
:type invertData: bool
:param axisTransformation: a permutation of the axes
:type axisTransformation: int
:param createNewDataset: if True, a new dataset will be generated. If False, the input dataset will be modified.
:type createNewDataset: bool

:return newDataset: inverted dataset. If createNewDataset is False, None is returned.
:rtype newDataset: ORSModel.ors.StructuredGrid
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
invertX = False

invertY = False

invertZ = False

invertData = False

axisTransformation = 1

createNewDataset = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
newDataset = OrsDatasetInvertor.invert(structuredGrid=structuredGrid,
                                       invertX=invertX,
                                       invertY=invertY,
                                       invertZ=invertZ,
                                       invertData=invertData,
                                       axisTransformation=axisTransformation,
                                       createNewDataset=createNewDataset)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# newDataset = orsObj('BC16B2FCB1DD43D0951A8B86101D520CCxvChannel')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets an object as representable and notifies the Dragonfly UI of a new available object

:name: publish
:execution: execute

:param newDataset: 
:type newDataset: ORSModel.ors.Managed
"""

# Interface method
newDataset.publish(logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Invert the data of a dataset along specified axes.

:name: invert
:execution: execute

:param structuredGrid: the dataset to invert
:type structuredGrid: ORSModel.ors.StructuredGrid
:param invertX_2: if True, the X axis will be inverted
:type invertX_2: bool
:param invertY_2: if True, the Y axis will be inverted
:type invertY_2: bool
:param invertZ_2: if True, the Z axis will be inverted
:type invertZ_2: bool
:param invertData_2: if True, the data will be inverted
:type invertData_2: bool
:param axisTransformation_2: a permutation of the axes
:type axisTransformation_2: int
:param createNewDataset_2: if True, a new dataset will be generated. If False, the input dataset will be modified.
:type createNewDataset_2: bool

:return newDataset_2: inverted dataset. If createNewDataset is False, None is returned.
:rtype newDataset_2: ORSModel.ors.StructuredGrid
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
invertX_2 = False

invertY_2 = False

invertZ_2 = False

invertData_2 = False

axisTransformation_2 = 4

createNewDataset_2 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
newDataset_2 = OrsDatasetInvertor.invert(structuredGrid=structuredGrid,
                                         invertX=invertX_2,
                                         invertY=invertY_2,
                                         invertZ=invertZ_2,
                                         invertData=invertData_2,
                                         axisTransformation=axisTransformation_2,
                                         createNewDataset=createNewDataset_2)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# newDataset_2 = orsObj('7B3D38C8AA914618BD4A6E39CF6C76ECCxvChannel')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets an object as representable and notifies the Dragonfly UI of a new available object

:name: publish
:execution: execute

:param newDataset_2: 
:type newDataset_2: ORSModel.ors.Managed
"""

# Interface method
newDataset_2.publish(logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: setTitle
:execution: execute

:param anInstanceOfManaged: 
:type anInstanceOfManaged: ORSModel.ors.Managed
:param newVal: 
:type newVal: str
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
newVal = 'XY'

# ----- END INPUT ARGUMENT DEFINITION ----- #

anInstanceOfManaged = structuredGrid
# Interface method
anInstanceOfManaged.setTitle(newVal=newVal,
                             logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: setTitle
:execution: execute

:param anInstanceOfManaged_2: 
:type anInstanceOfManaged_2: ORSModel.ors.Managed
:param newVal_2: 
:type newVal_2: str
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
newVal_2 = 'XZ'

# ----- END INPUT ARGUMENT DEFINITION ----- #

anInstanceOfManaged_2 = newDataset
# Interface method
anInstanceOfManaged_2.setTitle(newVal=newVal_2,
                               logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: setTitle
:execution: execute

:param anInstanceOfManaged_3: 
:type anInstanceOfManaged_3: ORSModel.ors.Managed
:param newVal_3: 
:type newVal_3: str
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
newVal_3 = 'YZ'

# ----- END INPUT ARGUMENT DEFINITION ----- #

anInstanceOfManaged_3 = newDataset_2
# Interface method
anInstanceOfManaged_3.setTitle(newVal=newVal_3,
                               logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Creates a new instance of ConversionType

:name: createConversionType
:execution: execute

:param isLabels: Convert to labels
:type isLabels: bool
:param outputTypeName: The conversion output type name as a string
:type outputTypeName: str
:param probabilityClassIdx: The class index used for ConversionType.OutputType.ClassProbabilities
:type probabilityClassIdx: int

:return aConversionType: new ConversionType instance
:rtype aConversionType: transient ConversionType
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
isLabels = True

outputTypeName = 'Confidence'

probabilityClassIdx = 1

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
aConversionType = AIInterfaceMethods.createConversionType(isLabels=isLabels,
                                                          outputTypeName=outputTypeName,
                                                          probabilityClassIdx=probabilityClassIdx)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# aConversionType = ConversionType(outputType=<OutputType.Labels: 1>, probabilityClassIdx=1)

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Creates a new instance of class Progress

:name: __new__
:execution: execute

:return aProgress: the created instance of class Progress
:rtype aProgress: ORSModel.ors.Progress
"""

# Interface method
aProgress = Progress(logging=True)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# aProgress = orsObj('E6FC0F260B9B481C8403BF21698A537DCxvProgress')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Creates a new instance of AIModelsManager

:name: getAIModelsManager
:execution: execute

:return modelManagerInstance: new AIModelsManager instance
:rtype modelManagerInstance: transient AIModelsManager
"""

# Interface method
modelManagerInstance = AIInterfaceMethods.getAIModelsManager()

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# modelManagerInstance = <ORSServiceClass.segmentation.model.aimodelsmanager.AIModelsManager object at 0x00000271472CFF40>

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Return an instance of AIModelAbstract

:name: getAIModel
:execution: execute

:param modelManagerInstance: A AIModelsManager instance
:type modelManagerInstance: transient AIModelsManager
:param modelId: model id
:type modelId: str

:return modelInstance: new AIModelAbstract instance
:rtype modelInstance: transient AIModelAbstract
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
modelId = 'Insert your model's UUID here'

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
modelInstance = AIInterfaceMethods.getAIModel(aiModelManager=modelManagerInstance,
                                              modelId=modelId)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# modelInstance = OnlyStem_UNet_2.5D_5Depth_11Slice_ef1413a02a1511f196e6001a7dda7115

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Apply an AI segmentation model.

:name: applySegmentationModel
:execution: execute

:param modelInstance: A AIModelAbstract instance
:type modelInstance: transient AIModelAbstract
:param modelManagerInstance: A AIModelsManager instance
:type modelManagerInstance: transient AIModelsManager
:param inputs: List of model inputs
:type inputs: ORSModel.ors.Channel
:count inputs: [1, None]
:param mask: Inference mask (only used if useMarkedSlice is False)
:type mask: ORSModel.ors.ROI
:param useMarkedSlices: Use marked slice as mask instead of using the mask.
:type useMarkedSlices: bool
:param inputSettingsList: Multi-Slice Input Settings list of dict
:type inputSettingsList: dict
:count inputSettingsList: [1, None]
:param normalizationTransformationsJSONData: Normalization Transformation list of dict
:type normalizationTransformationsJSONData: dict
:count normalizationTransformationsJSONData: [0, None]
:param aProgress: a Progress object
:type aProgress: ORSModel.ors.Progress
:param output: (optional) Object where the output labels/probabilities will be written. If not specified, new object will be created.
:type output: ORSModel.ors.StructuredGrid
:param offset: (optional) index of the first output voxel
:type offset: transient VoxelIndex
:param aConversionType: (optional) The conversion type (unconverted, labels, class probabilities, all probabilities or confidence)
:type aConversionType: transient ConversionType

:return ret_value: The model output
:rtype ret_value: ORSModel.ors.StructuredGrid
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
inputs = [anInstanceOfManaged]

mask = None

useMarkedSlices = False

inputSettingsListListElement = {'CHANNEL_COUNT': 11, 'REF_IDX': 5, 'INC_SLICE_IDX': 1}
inputSettingsList = [inputSettingsListListElement]

normalizationTransformationsJSONDataListElement = {'_slope': 1.0, '_offset': 0.0, '_min_possible_value': 0.0, '_max_possible_value': 65535.0, '_norm_min': 0.0, '_norm_max': 1.0, '_calib_min': 0.0, '_calib_max': 0.0, '_calib_min_key': '', '_calib_max_key': '', '_calibration_enabled': False, '_normalization_spread': 2.0, 'dim_unit_repr': "orsDimensionUnit(registrationKey='CANONICAL_DIMENSION_DENSITY', unitName='Density', unitAbbreviation='', unitType=COMWrapper.ORS_def.CxvUniverse_Dimension_Type.CXV_DIMENSION_CONTINUOUS_VARIABLE, conversionFactor=1, isImperial=False, calibrationValues={}, description='')"}
normalizationTransformationsJSONData = [normalizationTransformationsJSONDataListElement]

output = None

offset = None

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
ret_value = AIInterfaceMethods.applySegmentationModel(model=modelInstance,
                                                      modelManager=modelManagerInstance,
                                                      inputs=inputs,
                                                      mask=mask,
                                                      useMarkedSlices=useMarkedSlices,
                                                      inputSettingsList=inputSettingsList,
                                                      normalizationTransformationsJSONData=normalizationTransformationsJSONData,
                                                      progress=aProgress,
                                                      output=output,
                                                      offset=offset,
                                                      conversionType=aConversionType)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# ret_value = orsObj('307D9292038245EF903166056A95C221CxvLabeledMultiROI')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets the visibility of a ROI or MultiROI in all 2D views of the given scene layout

:name: setIsVisibleIn2DFromGenealogicalName
:execution: execute

:param name: a genealogical name of a scene layout
:type name: str
:param ret_value: a ROI or a MultiROI
:type ret_value: ORSModel.ors.ROI, ORSModel.ors.MultiROI
:param isVisible: True to set as visible, False otherwise
:type isVisible: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
name = 'toplayout\\scene_0'

isVisible = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
ROIHelper.setIsVisibleIn2DFromGenealogicalName(name=name,
                                               aROI=ret_value,
                                               isVisible=isVisible)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets an object as representable and notifies the Dragonfly UI of a new available object

:name: publish
:execution: execute

:param ret_value: 
:type ret_value: ORSModel.ors.Managed
"""

# Interface method
ret_value.publish(logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: deleteObject
:execution: execute

:param aProgress: 
:type aProgress: ORSModel.ors.Managed
"""

# Interface method
aProgress.deleteObject(logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Creates a new instance of ConversionType

:name: createConversionType
:execution: execute

:param isLabels_2: Convert to labels
:type isLabels_2: bool
:param outputTypeName_2: The conversion output type name as a string
:type outputTypeName_2: str
:param probabilityClassIdx_2: The class index used for ConversionType.OutputType.ClassProbabilities
:type probabilityClassIdx_2: int

:return aConversionType_2: new ConversionType instance
:rtype aConversionType_2: transient ConversionType
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
isLabels_2 = True

outputTypeName_2 = 'Confidence'

probabilityClassIdx_2 = 1

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
aConversionType_2 = AIInterfaceMethods.createConversionType(isLabels=isLabels_2,
                                                            outputTypeName=outputTypeName_2,
                                                            probabilityClassIdx=probabilityClassIdx_2)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# aConversionType_2 = ConversionType(outputType=<OutputType.Labels: 1>, probabilityClassIdx=1)

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Creates a new instance of class Progress

:name: __new__
:execution: execute

:return aProgress_2: the created instance of class Progress
:rtype aProgress_2: ORSModel.ors.Progress
"""

# Interface method
aProgress_2 = Progress(logging=True)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# aProgress_2 = orsObj('182153A0EAA14D19B3E6B8797F1D5743CxvProgress')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Creates a new instance of AIModelsManager

:name: getAIModelsManager
:execution: execute

:return modelManagerInstance_2: new AIModelsManager instance
:rtype modelManagerInstance_2: transient AIModelsManager
"""

# Interface method
modelManagerInstance_2 = AIInterfaceMethods.getAIModelsManager()

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# modelManagerInstance_2 = <ORSServiceClass.segmentation.model.aimodelsmanager.AIModelsManager object at 0x0000027181999B40>

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Return an instance of AIModelAbstract

:name: getAIModel
:execution: execute

:param modelManagerInstance_2: A AIModelsManager instance
:type modelManagerInstance_2: transient AIModelsManager
:param modelId_2: model id
:type modelId_2: str

:return modelInstance_2: new AIModelAbstract instance
:rtype modelInstance_2: transient AIModelAbstract
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
modelId_2 = 'Insert your model's UUID here'

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
modelInstance_2 = AIInterfaceMethods.getAIModel(aiModelManager=modelManagerInstance_2,
                                                modelId=modelId_2)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# modelInstance_2 = modelInstance

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Apply an AI segmentation model.

:name: applySegmentationModel
:execution: execute

:param modelInstance: A AIModelAbstract instance
:type modelInstance: transient AIModelAbstract
:param modelManagerInstance_2: A AIModelsManager instance
:type modelManagerInstance_2: transient AIModelsManager
:param inputs_2: List of model inputs
:type inputs_2: ORSModel.ors.Channel
:count inputs_2: [1, None]
:param mask_2: Inference mask (only used if useMarkedSlice is False)
:type mask_2: ORSModel.ors.ROI
:param useMarkedSlices_2: Use marked slice as mask instead of using the mask.
:type useMarkedSlices_2: bool
:param inputSettingsList_2: Multi-Slice Input Settings list of dict
:type inputSettingsList_2: dict
:count inputSettingsList_2: [1, None]
:param normalizationTransformationsJSONData_2: Normalization Transformation list of dict
:type normalizationTransformationsJSONData_2: dict
:count normalizationTransformationsJSONData_2: [0, None]
:param aProgress_2: a Progress object
:type aProgress_2: ORSModel.ors.Progress
:param output_2: (optional) Object where the output labels/probabilities will be written. If not specified, new object will be created.
:type output_2: ORSModel.ors.StructuredGrid
:param offset_2: (optional) index of the first output voxel
:type offset_2: transient VoxelIndex
:param aConversionType_2: (optional) The conversion type (unconverted, labels, class probabilities, all probabilities or confidence)
:type aConversionType_2: transient ConversionType

:return ret_value_2: The model output
:rtype ret_value_2: ORSModel.ors.StructuredGrid
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
inputs_2 = [anInstanceOfManaged_2]

mask_2 = None

useMarkedSlices_2 = False

inputSettingsListListElement_2 = {'CHANNEL_COUNT': 11, 'REF_IDX': 5, 'INC_SLICE_IDX': 1}
inputSettingsList_2 = [inputSettingsListListElement_2]

normalizationTransformationsJSONDataListElement_2 = {'_slope': 1.0, '_offset': 0.0, '_min_possible_value': 0.0, '_max_possible_value': 65535.0, '_norm_min': 0.0, '_norm_max': 1.0, '_calib_min': 0.0, '_calib_max': 0.0, '_calib_min_key': '', '_calib_max_key': '', '_calibration_enabled': False, '_normalization_spread': 2.0, 'dim_unit_repr': "orsDimensionUnit(registrationKey='CANONICAL_DIMENSION_DENSITY', unitName='Density', unitAbbreviation='', unitType=COMWrapper.ORS_def.CxvUniverse_Dimension_Type.CXV_DIMENSION_CONTINUOUS_VARIABLE, conversionFactor=1, isImperial=False, calibrationValues={}, description='')"}
normalizationTransformationsJSONData_2 = [normalizationTransformationsJSONDataListElement_2]

output_2 = None

offset_2 = None

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
ret_value_2 = AIInterfaceMethods.applySegmentationModel(model=modelInstance_2,
                                                        modelManager=modelManagerInstance_2,
                                                        inputs=inputs_2,
                                                        mask=mask_2,
                                                        useMarkedSlices=useMarkedSlices_2,
                                                        inputSettingsList=inputSettingsList_2,
                                                        normalizationTransformationsJSONData=normalizationTransformationsJSONData_2,
                                                        progress=aProgress_2,
                                                        output=output_2,
                                                        offset=offset_2,
                                                        conversionType=aConversionType_2)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# ret_value_2 = orsObj('508DB9D4B085434A881393322CCC17BACxvLabeledMultiROI')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets the visibility of a ROI or MultiROI in all 2D views of the given scene layout

:name: setIsVisibleIn2DFromGenealogicalName
:execution: execute

:param name_2: a genealogical name of a scene layout
:type name_2: str
:param ret_value_2: a ROI or a MultiROI
:type ret_value_2: ORSModel.ors.ROI, ORSModel.ors.MultiROI
:param isVisible_2: True to set as visible, False otherwise
:type isVisible_2: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
name_2 = 'toplayout\\scene_0'

isVisible_2 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
ROIHelper.setIsVisibleIn2DFromGenealogicalName(name=name_2,
                                               aROI=ret_value_2,
                                               isVisible=isVisible_2)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets an object as representable and notifies the Dragonfly UI of a new available object

:name: publish
:execution: execute

:param ret_value_2: 
:type ret_value_2: ORSModel.ors.Managed
"""

# Interface method
ret_value_2.publish(logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: deleteObject
:execution: execute

:param aProgress_2: 
:type aProgress_2: ORSModel.ors.Managed
"""

# Interface method
aProgress_2.deleteObject(logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Creates a new instance of ConversionType

:name: createConversionType
:execution: execute

:param isLabels_3: Convert to labels
:type isLabels_3: bool
:param outputTypeName_3: The conversion output type name as a string
:type outputTypeName_3: str
:param probabilityClassIdx_3: The class index used for ConversionType.OutputType.ClassProbabilities
:type probabilityClassIdx_3: int

:return aConversionType_3: new ConversionType instance
:rtype aConversionType_3: transient ConversionType
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
isLabels_3 = True

outputTypeName_3 = 'Confidence'

probabilityClassIdx_3 = 1

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
aConversionType_3 = AIInterfaceMethods.createConversionType(isLabels=isLabels_3,
                                                            outputTypeName=outputTypeName_3,
                                                            probabilityClassIdx=probabilityClassIdx_3)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# aConversionType_3 = ConversionType(outputType=<OutputType.Labels: 1>, probabilityClassIdx=1)

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Creates a new instance of class Progress

:name: __new__
:execution: execute

:return aProgress_3: the created instance of class Progress
:rtype aProgress_3: ORSModel.ors.Progress
"""

# Interface method
aProgress_3 = Progress(logging=True)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# aProgress_3 = orsObj('DB2B51FA58574B458BB33915AE734914CxvProgress')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Creates a new instance of AIModelsManager

:name: getAIModelsManager
:execution: execute

:return modelManagerInstance_3: new AIModelsManager instance
:rtype modelManagerInstance_3: transient AIModelsManager
"""

# Interface method
modelManagerInstance_3 = AIInterfaceMethods.getAIModelsManager()

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# modelManagerInstance_3 = <ORSServiceClass.segmentation.model.aimodelsmanager.AIModelsManager object at 0x000002718199A1D0>

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Return an instance of AIModelAbstract

:name: getAIModel
:execution: execute

:param modelManagerInstance_3: A AIModelsManager instance
:type modelManagerInstance_3: transient AIModelsManager
:param modelId_3: model id
:type modelId_3: str

:return modelInstance_3: new AIModelAbstract instance
:rtype modelInstance_3: transient AIModelAbstract
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
modelId_3 = 'Insert your model's UUID here'

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
modelInstance_3 = AIInterfaceMethods.getAIModel(aiModelManager=modelManagerInstance_3,
                                                modelId=modelId_3)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# modelInstance_3 = modelInstance

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Apply an AI segmentation model.

:name: applySegmentationModel
:execution: execute

:param modelInstance: A AIModelAbstract instance
:type modelInstance: transient AIModelAbstract
:param modelManagerInstance_3: A AIModelsManager instance
:type modelManagerInstance_3: transient AIModelsManager
:param inputs_3: List of model inputs
:type inputs_3: ORSModel.ors.Channel
:count inputs_3: [1, None]
:param mask_3: Inference mask (only used if useMarkedSlice is False)
:type mask_3: ORSModel.ors.ROI
:param useMarkedSlices_3: Use marked slice as mask instead of using the mask.
:type useMarkedSlices_3: bool
:param inputSettingsList_3: Multi-Slice Input Settings list of dict
:type inputSettingsList_3: dict
:count inputSettingsList_3: [1, None]
:param normalizationTransformationsJSONData_3: Normalization Transformation list of dict
:type normalizationTransformationsJSONData_3: dict
:count normalizationTransformationsJSONData_3: [0, None]
:param aProgress_3: a Progress object
:type aProgress_3: ORSModel.ors.Progress
:param output_3: (optional) Object where the output labels/probabilities will be written. If not specified, new object will be created.
:type output_3: ORSModel.ors.StructuredGrid
:param offset_3: (optional) index of the first output voxel
:type offset_3: transient VoxelIndex
:param aConversionType_3: (optional) The conversion type (unconverted, labels, class probabilities, all probabilities or confidence)
:type aConversionType_3: transient ConversionType

:return ret_value_3: The model output
:rtype ret_value_3: ORSModel.ors.StructuredGrid
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
inputs_3 = [anInstanceOfManaged_3]

mask_3 = None

useMarkedSlices_3 = False

inputSettingsListListElement_3 = {'CHANNEL_COUNT': 11, 'REF_IDX': 5, 'INC_SLICE_IDX': 1}
inputSettingsList_3 = [inputSettingsListListElement_3]

normalizationTransformationsJSONDataListElement_3 = {'_slope': 1.0, '_offset': 0.0, '_min_possible_value': 0.0, '_max_possible_value': 65535.0, '_norm_min': 0.0, '_norm_max': 1.0, '_calib_min': 0.0, '_calib_max': 0.0, '_calib_min_key': '', '_calib_max_key': '', '_calibration_enabled': False, '_normalization_spread': 2.0, 'dim_unit_repr': "orsDimensionUnit(registrationKey='CANONICAL_DIMENSION_DENSITY', unitName='Density', unitAbbreviation='', unitType=COMWrapper.ORS_def.CxvUniverse_Dimension_Type.CXV_DIMENSION_CONTINUOUS_VARIABLE, conversionFactor=1, isImperial=False, calibrationValues={}, description='')"}
normalizationTransformationsJSONData_3 = [normalizationTransformationsJSONDataListElement_3]

output_3 = None

offset_3 = None

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
ret_value_3 = AIInterfaceMethods.applySegmentationModel(model=modelInstance_3,
                                                        modelManager=modelManagerInstance_3,
                                                        inputs=inputs_3,
                                                        mask=mask_3,
                                                        useMarkedSlices=useMarkedSlices_3,
                                                        inputSettingsList=inputSettingsList_3,
                                                        normalizationTransformationsJSONData=normalizationTransformationsJSONData_3,
                                                        progress=aProgress_3,
                                                        output=output_3,
                                                        offset=offset_3,
                                                        conversionType=aConversionType_3)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# ret_value_3 = orsObj('4A39FEDC28664687BF7E3F93E8F01F56CxvLabeledMultiROI')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets the visibility of a ROI or MultiROI in all 2D views of the given scene layout

:name: setIsVisibleIn2DFromGenealogicalName
:execution: execute

:param name_3: a genealogical name of a scene layout
:type name_3: str
:param ret_value_3: a ROI or a MultiROI
:type ret_value_3: ORSModel.ors.ROI, ORSModel.ors.MultiROI
:param isVisible_3: True to set as visible, False otherwise
:type isVisible_3: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
name_3 = 'toplayout\\scene_0'

isVisible_3 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
ROIHelper.setIsVisibleIn2DFromGenealogicalName(name=name_3,
                                               aROI=ret_value_3,
                                               isVisible=isVisible_3)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets an object as representable and notifies the Dragonfly UI of a new available object

:name: publish
:execution: execute

:param ret_value_3: 
:type ret_value_3: ORSModel.ors.Managed
"""

# Interface method
ret_value_3.publish(logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: deleteObject
:execution: execute

:param aProgress_3: 
:type aProgress_3: ORSModel.ors.Managed
"""

# Interface method
aProgress_3.deleteObject(logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Selected/unselect the given MultiROI labels specified in the listOfLabels list

:name: setSelectedLabels
:execution: execute

:param ret_value: input MultiROI
:type ret_value: ORSModel.ors.MultiROI
:param timeStep: time step where tp select
:type timeStep: int
:param listOfLabels: a python list of the selected label
:type listOfLabels: int
:count listOfLabels: [0, None]
:param selected: select or unselect
:type selected: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
timeStep = 0

listOfLabelsListElement = 1
listOfLabels = [listOfLabelsListElement]

selected = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
OrsMultiROILabelInformationWidget.setSelectedLabels(multiROI=ret_value,
                                                    timeStep=timeStep,
                                                    listOfLabels=listOfLabels,
                                                    selected=selected)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Extracts each selected label from a Multi-ROI into a separate ROI.

:name: extractSelectedLabelsToROIs
:execution: execute

:param ret_value: a Multi-ROI
:type ret_value: ORSModel.ors.MultiROI

:return roiExtracted: list of created ROIs
:rtype roiExtracted: ORSModel.ors.ROI
:rcount roiExtracted: [0, None]
:return roiExtractedListElement: extracted value at index #0 from roiExtracted
:rtype roiExtractedListElement: ORSModel.ors.ROI
"""

# Interface method
roiExtracted = MultiROILabelHelper.extractSelectedLabelsToROIs(multiroi=ret_value)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
roiExtractedListElement = roiExtracted[0]
# roiExtractedListElement = orsObj('5E112056442F41F29B814E34370FED28CxvVolume_ROI')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets an object as representable and notifies the Dragonfly UI of a new available object

:name: publish
:execution: execute

:param roiExtractedListElement: 
:type roiExtractedListElement: ORSModel.ors.Managed
"""

# Interface method
roiExtractedListElement.publish(logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: setTitle
:execution: execute

:param roiExtractedListElement: 
:type roiExtractedListElement: ORSModel.ors.Managed
:param newVal_4: 
:type newVal_4: str
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
newVal_4 = 'Model Prediction on XY'

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
roiExtractedListElement.setTitle(newVal=newVal_4,
                                 logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Selected/unselect the given MultiROI labels specified in the listOfLabels list

:name: setSelectedLabels
:execution: execute

:param ret_value_2: input MultiROI
:type ret_value_2: ORSModel.ors.MultiROI
:param timeStep_2: time step where tp select
:type timeStep_2: int
:param listOfLabels_2: a python list of the selected label
:type listOfLabels_2: int
:count listOfLabels_2: [0, None]
:param selected_2: select or unselect
:type selected_2: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
timeStep_2 = 0

listOfLabelsListElement_2 = 1
listOfLabels_2 = [listOfLabelsListElement_2]

selected_2 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
OrsMultiROILabelInformationWidget.setSelectedLabels(multiROI=ret_value_2,
                                                    timeStep=timeStep_2,
                                                    listOfLabels=listOfLabels_2,
                                                    selected=selected_2)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Extracts each selected label from a Multi-ROI into a separate ROI.

:name: extractSelectedLabelsToROIs
:execution: execute

:param ret_value_2: a Multi-ROI
:type ret_value_2: ORSModel.ors.MultiROI

:return roiExtracted_2: list of created ROIs
:rtype roiExtracted_2: ORSModel.ors.ROI
:rcount roiExtracted_2: [0, None]
:return roiExtractedListElement_2: extracted value at index #0 from roiExtracted_2
:rtype roiExtractedListElement_2: ORSModel.ors.ROI
"""

# Interface method
roiExtracted_2 = MultiROILabelHelper.extractSelectedLabelsToROIs(multiroi=ret_value_2)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
roiExtractedListElement_2 = roiExtracted_2[0]
# roiExtractedListElement_2 = orsObj('AA17C3B0A6D048AB94004B44B2406D45CxvVolume_ROI')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets an object as representable and notifies the Dragonfly UI of a new available object

:name: publish
:execution: execute

:param roiExtractedListElement_2: 
:type roiExtractedListElement_2: ORSModel.ors.Managed
"""

# Interface method
roiExtractedListElement_2.publish(logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: setTitle
:execution: execute

:param roiExtractedListElement_2: 
:type roiExtractedListElement_2: ORSModel.ors.Managed
:param newVal_5: 
:type newVal_5: str
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
newVal_5 = 'Model Prediction on XZ'

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
roiExtractedListElement_2.setTitle(newVal=newVal_5,
                                   logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: setTitle
:execution: execute

:param ret_value_3: 
:type ret_value_3: ORSModel.ors.Managed
:param newVal_6: 
:type newVal_6: str
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
newVal_6 = 'Segmentation OnlyStem_UNet_2.5D_5Depth_11Slice'

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
ret_value_3.setTitle(newVal=newVal_6,
                     logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Selected/unselect the given MultiROI labels specified in the listOfLabels list

:name: setSelectedLabels
:execution: execute

:param ret_value_3: input MultiROI
:type ret_value_3: ORSModel.ors.MultiROI
:param timeStep_3: time step where tp select
:type timeStep_3: int
:param listOfLabels_3: a python list of the selected label
:type listOfLabels_3: int
:count listOfLabels_3: [0, None]
:param selected_3: select or unselect
:type selected_3: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
timeStep_3 = 0

listOfLabelsListElement_3 = 1
listOfLabels_3 = [listOfLabelsListElement_3]

selected_3 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
OrsMultiROILabelInformationWidget.setSelectedLabels(multiROI=ret_value_3,
                                                    timeStep=timeStep_3,
                                                    listOfLabels=listOfLabels_3,
                                                    selected=selected_3)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Extracts each selected label from a Multi-ROI into a separate ROI.

:name: extractSelectedLabelsToROIs
:execution: execute

:param ret_value_3: a Multi-ROI
:type ret_value_3: ORSModel.ors.MultiROI

:return roiExtracted_3: list of created ROIs
:rtype roiExtracted_3: ORSModel.ors.ROI
:rcount roiExtracted_3: [0, None]
:return roiExtractedListElement_3: extracted value at index #0 from roiExtracted_3
:rtype roiExtractedListElement_3: ORSModel.ors.ROI
"""

# Interface method
roiExtracted_3 = MultiROILabelHelper.extractSelectedLabelsToROIs(multiroi=ret_value_3)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
roiExtractedListElement_3 = roiExtracted_3[0]
# roiExtractedListElement_3 = orsObj('0D8BAF9E28E940D99C15D724D1AB904FCxvVolume_ROI')

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets an object as representable and notifies the Dragonfly UI of a new available object

:name: publish
:execution: execute

:param roiExtractedListElement_3: 
:type roiExtractedListElement_3: ORSModel.ors.Managed
"""

# Interface method
roiExtractedListElement_3.publish(logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: setTitle
:execution: execute

:param roiExtractedListElement_3: 
:type roiExtractedListElement_3: ORSModel.ors.Managed
:param newVal_7: 
:type newVal_7: str
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
newVal_7 = 'Model Prediction on XY'

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
roiExtractedListElement_3.setTitle(newVal=newVal_7,
                                   logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Invert the data of a dataset along specified axes.

:name: invert
:execution: execute

:param roiExtractedListElement_2: the dataset to invert
:type roiExtractedListElement_2: ORSModel.ors.StructuredGrid
:param invertX: if True, the X axis will be inverted
:type invertX: bool
:param invertY: if True, the Y axis will be inverted
:type invertY: bool
:param invertZ: if True, the Z axis will be inverted
:type invertZ: bool
:param invertData: if True, the data will be inverted
:type invertData: bool
:param axisTransformation: a permutation of the axes
:type axisTransformation: int
:param createNewDataset: if True, a new dataset will be generated. If False, the input dataset will be modified.
:type createNewDataset: bool

:return newDataset: inverted dataset. If createNewDataset is False, None is returned.
:rtype newDataset: ORSModel.ors.StructuredGrid
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
invertX = False

invertY = False

invertZ = False

invertData = False

axisTransformation = 1

createNewDataset = False

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
newDataset = OrsDatasetInvertor.invert(structuredGrid=roiExtractedListElement_2,
                                       invertX=invertX,
                                       invertY=invertY,
                                       invertZ=invertZ,
                                       invertData=invertData,
                                       axisTransformation=axisTransformation,
                                       createNewDataset=createNewDataset)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# newDataset = None

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Invert the data of a dataset along specified axes.

:name: invert
:execution: execute

:param roiExtractedListElement_3: the dataset to invert
:type roiExtractedListElement_3: ORSModel.ors.StructuredGrid
:param invertX_2: if True, the X axis will be inverted
:type invertX_2: bool
:param invertY_2: if True, the Y axis will be inverted
:type invertY_2: bool
:param invertZ_2: if True, the Z axis will be inverted
:type invertZ_2: bool
:param invertData_2: if True, the data will be inverted
:type invertData_2: bool
:param axisTransformation_2: a permutation of the axes
:type axisTransformation_2: int
:param createNewDataset_2: if True, a new dataset will be generated. If False, the input dataset will be modified.
:type createNewDataset_2: bool

:return newDataset_2: inverted dataset. If createNewDataset is False, None is returned.
:rtype newDataset_2: ORSModel.ors.StructuredGrid
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
invertX_2 = False

invertY_2 = False

invertZ_2 = False

invertData_2 = False

axisTransformation_2 = 3

createNewDataset_2 = False

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
newDataset_2 = OrsDatasetInvertor.invert(structuredGrid=roiExtractedListElement_3,
                                         invertX=invertX_2,
                                         invertY=invertY_2,
                                         invertZ=invertZ_2,
                                         invertData=invertData_2,
                                         axisTransformation=axisTransformation_2,
                                         createNewDataset=createNewDataset_2)

# ----- BEGIN RETURNED VALUES DEFINITION ----- #
# newDataset_2 = None

# ----- END RETURNED VALUES DEFINITION ----- #
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: setTitle
:execution: execute

:param roiExtractedListElement_2: 
:type roiExtractedListElement_2: ORSModel.ors.Managed
:param newVal_8: 
:type newVal_8: str
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
newVal_8 = 'Model Prediction on XZ'

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
roiExtractedListElement_2.setTitle(newVal=newVal_8,
                                   logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
:name: setTitle
:execution: execute

:param roiExtractedListElement_3: 
:type roiExtractedListElement_3: ORSModel.ors.Managed
:param newVal_9: 
:type newVal_9: str
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
newVal_9 = 'Model Prediction on YZ'

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
roiExtractedListElement_3.setTitle(newVal=newVal_9,
                                   logging=True)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets the visibility of a ROI or MultiROI in all 2D views of the given scene layout

:name: setIsVisibleIn2DFromGenealogicalName
:execution: execute

:param name_4: a genealogical name of a scene layout
:type name_4: str
:param ret_value_3: a ROI or a MultiROI
:type ret_value_3: ORSModel.ors.ROI, ORSModel.ors.MultiROI
:param isVisible_4: True to set as visible, False otherwise
:type isVisible_4: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
name_4 = 'toplayout\\scene_0'

isVisible_4 = False

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
ROIHelper.setIsVisibleIn2DFromGenealogicalName(name=name_4,
                                               aROI=ret_value_3,
                                               isVisible=isVisible_4)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets the visibility of a ROI or MultiROI in all 2D views of the given scene layout

:name: setIsVisibleIn2DFromGenealogicalName
:execution: execute

:param name_5: a genealogical name of a scene layout
:type name_5: str
:param ret_value_2: a ROI or a MultiROI
:type ret_value_2: ORSModel.ors.ROI, ORSModel.ors.MultiROI
:param isVisible_5: True to set as visible, False otherwise
:type isVisible_5: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
name_5 = 'toplayout\\scene_0'

isVisible_5 = False

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
ROIHelper.setIsVisibleIn2DFromGenealogicalName(name=name_5,
                                               aROI=ret_value_2,
                                               isVisible=isVisible_5)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets the visibility of a ROI or MultiROI in all 2D views of the given scene layout

:name: setIsVisibleIn2DFromGenealogicalName
:execution: execute

:param name_6: a genealogical name of a scene layout
:type name_6: str
:param ret_value: a ROI or a MultiROI
:type ret_value: ORSModel.ors.ROI, ORSModel.ors.MultiROI
:param isVisible_6: True to set as visible, False otherwise
:type isVisible_6: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
name_6 = 'toplayout\\scene_0'

isVisible_6 = False

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
ROIHelper.setIsVisibleIn2DFromGenealogicalName(name=name_6,
                                               aROI=ret_value,
                                               isVisible=isVisible_6)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets the visibility of a ROI or MultiROI in all 2D views of the given scene layout

:name: setIsVisibleIn2DFromGenealogicalName
:execution: execute

:param name_7: a genealogical name of a scene layout
:type name_7: str
:param roiExtractedListElement: a ROI or a MultiROI
:type roiExtractedListElement: ORSModel.ors.ROI, ORSModel.ors.MultiROI
:param isVisible_7: True to set as visible, False otherwise
:type isVisible_7: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
name_7 = 'toplayout\\scene_0'

isVisible_7 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
ROIHelper.setIsVisibleIn2DFromGenealogicalName(name=name_7,
                                               aROI=roiExtractedListElement,
                                               isVisible=isVisible_7)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets the visibility of a ROI or MultiROI in all 2D views of the given scene layout

:name: setIsVisibleIn2DFromGenealogicalName
:execution: execute

:param name_8: a genealogical name of a scene layout
:type name_8: str
:param roiExtractedListElement_2: a ROI or a MultiROI
:type roiExtractedListElement_2: ORSModel.ors.ROI, ORSModel.ors.MultiROI
:param isVisible_8: True to set as visible, False otherwise
:type isVisible_8: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
name_8 = 'toplayout\\scene_0'

isVisible_8 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
ROIHelper.setIsVisibleIn2DFromGenealogicalName(name=name_8,
                                               aROI=roiExtractedListElement_2,
                                               isVisible=isVisible_8)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets the visibility of a ROI or MultiROI in all 2D views of the given scene layout

:name: setIsVisibleIn2DFromGenealogicalName
:execution: execute

:param name_9: a genealogical name of a scene layout
:type name_9: str
:param roiExtractedListElement_3: a ROI or a MultiROI
:type roiExtractedListElement_3: ORSModel.ors.ROI, ORSModel.ors.MultiROI
:param isVisible_9: True to set as visible, False otherwise
:type isVisible_9: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
name_9 = 'toplayout\\scene_0'

isVisible_9 = True

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
ROIHelper.setIsVisibleIn2DFromGenealogicalName(name=name_9,
                                               aROI=roiExtractedListElement_3,
                                               isVisible=isVisible_9)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets the visibility of a ROI or MultiROI in all 2D views of the given scene layout

:name: setIsVisibleIn2DFromGenealogicalName
:execution: execute

:param name_10: a genealogical name of a scene layout
:type name_10: str
:param roiExtractedListElement_3: a ROI or a MultiROI
:type roiExtractedListElement_3: ORSModel.ors.ROI, ORSModel.ors.MultiROI
:param isVisible_10: True to set as visible, False otherwise
:type isVisible_10: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
name_10 = 'toplayout\\scene_0'

isVisible_10 = False

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
ROIHelper.setIsVisibleIn2DFromGenealogicalName(name=name_10,
                                               aROI=roiExtractedListElement_3,
                                               isVisible=isVisible_10)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets the visibility of a ROI or MultiROI in all 2D views of the given scene layout

:name: setIsVisibleIn2DFromGenealogicalName
:execution: execute

:param name_11: a genealogical name of a scene layout
:type name_11: str
:param roiExtractedListElement_2: a ROI or a MultiROI
:type roiExtractedListElement_2: ORSModel.ors.ROI, ORSModel.ors.MultiROI
:param isVisible_11: True to set as visible, False otherwise
:type isVisible_11: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
name_11 = 'toplayout\\scene_0'

isVisible_11 = False

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
ROIHelper.setIsVisibleIn2DFromGenealogicalName(name=name_11,
                                               aROI=roiExtractedListElement_2,
                                               isVisible=isVisible_11)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Sets the visibility of a ROI or MultiROI in all 2D views of the given scene layout

:name: setIsVisibleIn2DFromGenealogicalName
:execution: execute

:param name_12: a genealogical name of a scene layout
:type name_12: str
:param roiExtractedListElement: a ROI or a MultiROI
:type roiExtractedListElement: ORSModel.ors.ROI, ORSModel.ors.MultiROI
:param isVisible_12: True to set as visible, False otherwise
:type isVisible_12: bool
"""

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #
name_12 = 'toplayout\\scene_0'

isVisible_12 = False

# ----- END INPUT ARGUMENT DEFINITION ----- #
# Interface method
ROIHelper.setIsVisibleIn2DFromGenealogicalName(name=name_12,
                                               aROI=roiExtractedListElement,
                                               isVisible=isVisible_12)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #

"""
Combines the 3 Multi.ROI outputs from the segmentation models, keeping only areas that are the same in at least 2/3 prediction planes

:name: 2/3 Planes Union
:execution: execute

:param XY: Model's prediction on the XY image plane
:type XY: ORSModel.ors.ROI, ORSModel.ors.MultiROI
:param XZ: Model's prediction on the XZ image plane
:type XZ: ORSModel.ors.ROI, ORSModel.ors.MultiROI
:param YZ: Model's prediction on the YZ image plane
:type YZ: ORSModel.ors.ROI, ORSModel.ors.MultiROI
:param XY_XZ: Intersection of the XY and XZ image planes
:type XY_XZ: ORSModel.ors.ROI, ORSModel.ors.MultiROI
:param XY_YZ: Intersection of the XY and YZ image planes
:type XY_YZ: ORSModel.ors.ROI, ORSModel.ors.MultiROI
:param XZ_YZ: Intersection of the XZ and YZ image planes
:type XZ_YZ: ORSModel.ors.ROI, ORSModel.ors.MultiROI
"""
import ORSModel

# ----- BEGIN INPUT ARGUMENT DEFINITION ----- #

XY = roiExtractedListElement
XZ = roiExtractedListElement_2
YZ = roiExtractedListElement_3

# ----- END INPUT ARGUMENT DEFINITION ----- #

# Intersect each prediction i.e. isolates sections of the model outputs where 2/3 of the models agree 

XY_XZ = XY.getIntersectionWithROI(XZ, None)
XY_XZ.setTitle("XY_XZ")
XY_XZ.publish()

XY_YZ = XY.getIntersectionWithROI(YZ, None)
XY_YZ.setTitle("XY_YZ")
XY_YZ.publish()

XZ_YZ = XZ.getIntersectionWithROI(YZ, None)
XZ_YZ.setTitle("XZ_YZ")
XZ_YZ.publish()

# Calculates and returns the union of the three intersections 

FINAL = XY_XZ.copy()     
FINAL.addROI(XY_YZ)
FINAL.addROI(XZ_YZ)

FINAL.setTitle("Union")
FINAL.publish()

print("Done.")
# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #d
"""
Deletes a ROI

:name: deleteROI
:execution: execute

:param aROI: the ROI to delete
:type aROI: ORSModel.ors.ROI
"""

# Interface method
DisplayROI.deleteROI(aROI=XY)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Deletes a ROI

:name: deleteROI
:execution: execute

:param aROI_2: the ROI to delete
:type aROI_2: ORSModel.ors.ROI
"""

# Interface method
DisplayROI.deleteROI(aROI=XZ)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Deletes a ROI

:name: deleteROI
:execution: execute

:param aROI_3: the ROI to delete
:type aROI_3: ORSModel.ors.ROI
"""

# Interface method
DisplayROI.deleteROI(aROI=YZ)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Deletes a ROI

:name: deleteROI
:execution: execute

:param aROI_4: the ROI to delete
:type aROI_4: ORSModel.ors.ROI
"""

# Interface method
DisplayROI.deleteROI(aROI=XY_XZ)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Deletes a ROI

:name: deleteROI
:execution: execute

:param aROI_5: the ROI to delete
:type aROI_5: ORSModel.ors.ROI
"""

# Interface method
DisplayROI.deleteROI(aROI=XY_YZ)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Deletes a ROI

:name: deleteROI
:execution: execute

:param aROI_6: the ROI to delete
:type aROI_6: ORSModel.ors.ROI
"""

# Interface method
DisplayROI.deleteROI(aROI=XZ_YZ)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Deletes a MultiROI

:name: deleteMultiROI
:execution: execute

:param aMultiROI: the MultiROI to delete
:type aMultiROI: ORSModel.ors.MultiROI
"""

# Interface method
DisplayROI.deleteMultiROI(aMultiROI=ret_value)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Deletes a MultiROI

:name: deleteMultiROI
:execution: execute

:param aMultiROI_2: the MultiROI to delete
:type aMultiROI_2: ORSModel.ors.MultiROI
"""

# Interface method
DisplayROI.deleteMultiROI(aMultiROI=ret_value_2)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Deletes a MultiROI

:name: deleteMultiROI
:execution: execute

:param aMultiROI_3: the MultiROI to delete
:type aMultiROI_3: ORSModel.ors.MultiROI
"""

# Interface method
DisplayROI.deleteMultiROI(aMultiROI=ret_value_3)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Deletes a dataset

:name: deleteDataset
:execution: execute

:param aDataset: the dataset to delete
:type aDataset: ORSModel.ors.Channel
"""

# Interface method
DatasetHelper.deleteDataset(aDataset=anInstanceOfManaged_2)

# ********** END MACRO ********** #

# ********** BEGIN MACRO ********** #
"""
Deletes a dataset

:name: deleteDataset
:execution: execute

:param aDataset_2: the dataset to delete
:type aDataset_2: ORSModel.ors.Channel
"""

# Interface method
DatasetHelper.deleteDataset(aDataset=anInstanceOfManaged_3)

# ********** END MACRO ********** #