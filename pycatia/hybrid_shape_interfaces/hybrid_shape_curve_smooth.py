#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.angle import Angle
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeCurveSmooth(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeCurveSmooth
                | 
                | Represents the hybrid shape curve smoothing operation feature.
                | Role: To access the data of the curve smoothing operation.of the hybrid shape
                | curve parameter object. This data includes:
                | 
                |     The curve to smooth
                |     The support (if exist )
                |     The tangent tolerance value (threshold)
                |     The curvature tolerance value (threshold)
                |     The info if curvature threshold is activated
                |     The maximum deviation accepted
                |     The info if maxcimum deviation is activated
                |     The fixed points
                |     The fixed segments
                |     The info if topology simplification is activated
                | 
                | Use the HybridShapeFactory.AddNewCurveSmooth to create a HybridShapeCurveSmooth
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_curve_smooth = com_object

    @property
    def correction_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property CorrectionMode() As long
                | 
                |     Returns or sets the correction mode (threshold, point, tangency or
                |     curvature) applied to the smoothed curve.
                |     Legal values:
                | 
                |     0
                |         CATGSMCSCorrectionMode_Threshold. no continuity 
                |     1
                |         CATGSMCSCorrectionMode_Point. continuity in point
                |         (C0).
                |     2
                |         CATGSMCSCorrectionMode_Tangency. continuity in tangency
                |         (C1).
                |     3
                |         CATGSMCSCorrectionMode_Curvature. continuity in curvature
                |         (C2).
                | 
                | Example:
                |     This example retrieves in oMode the correction mode for the
                |     hybShpCurveSmooth hybrid shape feature.
                | 
                |      oMode = hybShpCurveSmooth.CorrectionMode

        :return: int
        """

        return self.hybrid_shape_curve_smooth.CorrectionMode

    @correction_mode.setter
    def correction_mode(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_curve_smooth.CorrectionMode = value

    @property
    def curvature_threshold(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property CurvatureThreshold() As double
                | 
                |     Returns or sets the CurvatureThreshold.
                | 
                |     Example: This example retrieves the CurvatureThreshold of the
                |     hybShpCurveSmooth in CurvatureThH.
                | 
                |      Dim CurvatureThH as double
                |      CurvatureThH = hybShpCurvePar.CurvatureThreshold

        :return: float
        """

        return self.hybrid_shape_curve_smooth.CurvatureThreshold

    @curvature_threshold.setter
    def curvature_threshold(self, value):
        """
        :param float value:
        """

        self.hybrid_shape_curve_smooth.CurvatureThreshold = value

    @property
    def curvature_threshold_activity(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property CurvatureThresholdActivity() As boolean
                | 
                |     Returns or sets the CurvatureThresholdActivity.
                | 
                |     Example: This example retrieves the CurvatureThresholdActivity of the
                |     hybShpCurveSmooth in CurvatureActivity .
                | 
                |      Dim CurvatureActivity as boolean 
                |      CurvatureActivity = hybShpCurvePar.CurvatureThresholdActivity

        :return: bool
        """

        return self.hybrid_shape_curve_smooth.CurvatureThresholdActivity

    @curvature_threshold_activity.setter
    def curvature_threshold_activity(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_curve_smooth.CurvatureThresholdActivity = value

    @property
    def curve_to_smooth(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property CurveToSmooth() As Reference
                | 
                |     Returns or sets the curve to smooth.
                | 
                |     Example: This example retrieves the curve to smooth object of the
                |     hybShpCurveSmooth in Curve.
                | 
                |      Dim Curve as CATIAReference 
                |      Curve  = hybShpCurvePar.CurveToSmooth

        :return: Reference
        """

        return Reference(self.hybrid_shape_curve_smooth.CurveToSmooth)

    @curve_to_smooth.setter
    def curve_to_smooth(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_curve_smooth.CurveToSmooth = value

    @property
    def end_extremity_continuity(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property EndExtremityContinuity() As long
                | 
                |     Returns or sets the continuity condition (curvature, tangency or point)
                |     applied to the smoothed curve with regard to the input curve at the end
                |     extremity of the input curve.
                |     Legal values:
                | 
                |     0
                |         CATGSMContinuity_Point. continuity in point (C0). 
                |     1
                |         CATGSMContinuity_Tangency. continuity in tangency
                |         (C1).
                |     2
                |         CATGSMContinuity_Curvature. continuity in curvature
                |         (C2).
                | 
                | Example:
                |     This example retrieves in oContinuity the continuity at the end extremity
                |     for the hybShpCurveSmooth hybrid shape feature.
                | 
                |      oContinuity = hybShpCurveSmooth.EndExtremityContinuity

        :return: int
        """

        return self.hybrid_shape_curve_smooth.EndExtremityContinuity

    @end_extremity_continuity.setter
    def end_extremity_continuity(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_curve_smooth.EndExtremityContinuity = value

    @property
    def maximum_deviation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property MaximumDeviation() As Length (Read Only)
                | 
                |     Returns the MaximumDeviation.
                | 
                |     Example: This example retrieves the MaximumDeviation of the
                |     hybShpCurveSmooth in MaximumDeviationVal.
                | 
                |      Dim MaximumDeviationVal as CATIALength
                |      MaximumDeviationVal  = hybShpCurvePar.MaximumDeviation

        :return: Length
        """

        return Length(self.hybrid_shape_curve_smooth.MaximumDeviation)

    @property
    def maximum_deviation_activity(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property MaximumDeviationActivity() As boolean
                | 
                |     Returns or sets the MaximumDeviationActivity.
                | 
                |     Example: This example retrieves the MaximumDeviationActivity of the
                |     hybShpCurveSmooth in MaxActivity .
                | 
                |      Dim MaxActivity as boolean
                |      MaxActivity  = hybShpCurvePar.MaximumDeviationActivity

        :return: bool
        """

        return self.hybrid_shape_curve_smooth.MaximumDeviationActivity

    @maximum_deviation_activity.setter
    def maximum_deviation_activity(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_curve_smooth.MaximumDeviationActivity = value

    @property
    def start_extremity_continuity(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property StartExtremityContinuity() As long
                | 
                |     Returns or sets the continuity condition (curvature, tangency or point)
                |     applied to the smoothed curve with regard to the input curve at the start
                |     extremity of the input curve.
                |     Legal values:
                | 
                |     0
                |         CATGSMContinuity_Point. continuity in point (C0). 
                |     1
                |         CATGSMContinuity_Tangency. continuity in tangency
                |         (C1).
                |     2
                |         CATGSMContinuity_Curvature. continuity in curvature
                |         (C2).
                | 
                | Example:
                |     This example retrieves in oContinuity the continuity at the start extremity
                |     for the hybShpCurveSmooth hybrid shape feature.
                | 
                |      oContinuity = hybShpCurveSmooth.StartExtremityContinuity

        :return: int
        """

        return self.hybrid_shape_curve_smooth.StartExtremityContinuity

    @start_extremity_continuity.setter
    def start_extremity_continuity(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_curve_smooth.StartExtremityContinuity = value

    @property
    def support(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Support() As Reference
                | 
                |     Returns or sets the support of the curve.
                |     if Suppport == nothing no support associated to the curve
                | 
                |     Example: This example retrieves the support of curve to smooth object of
                |     the hybShpCurveSmooth in Support.
                | 
                |      Dim Support  as CATIAReference 
                |      Support   = ybShpCurveSmooth.Support

        :return: Reference
        """

        return Reference(self.hybrid_shape_curve_smooth.Support)

    @support.setter
    def support(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_curve_smooth.Support = value

    @property
    def tangency_threshold(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property TangencyThreshold() As Angle (Read Only)
                | 
                |     Returns the TangencyThreshold.
                | 
                |     Example: This example retrieves the curve to smooth object of the
                |     hybShpCurveSmooth in AngleThH.
                | 
                |      Dim Curve as CATIAAngle  
                |      AngleThH  = ybShpCurveSmooth.TangencyThreshold

        :return: Angle
        """

        return Angle(self.hybrid_shape_curve_smooth.TangencyThreshold)

    @property
    def topology_simplification_activity(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property TopologySimplificationActivity() As boolean
                | 
                |     Returns or sets the TopologySimplificationActivity.
                | 
                |     Example: This example retrieves the TopologySimplificationActivity of the
                |     hybShpCurveSmooth in TopSimplifyAct.
                | 
                |      Dim TopSimplifyAct as boolean 
                |      TopSimplifyAct  = hybShpCurvePar.TogologySimplificationActivity 
                |      
                | 
                |     Methods
                | 
                | o Sub AddFrozenCurveSegment(Reference iCurve)
                | 
                |     Adds a frozen curve to the hybrid shape curve smooth feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iCurve
                |             The curve to be added to the hybrid shape curve smooth feature
                |             object. 
                | 
                |     Example:
                |         The following example adds the iCurve curve to the hybShpCurveSmooth
                |         object.
                | 
                |          hybShpCurveSmooth.AddFrozenCurveSegment iCurve
                |          
                | 
                | o Sub AddFrozenPoint(Reference iPoint)
                | 
                |     Adds a frozen points to the hybrid shape curve smooth feature
                |     object.
                | 
                |     Parameters:
                | 
                |         iPoint
                |             The frozen point to be added to the hybrid shape curve smooth
                |             feature object. 
                | 
                |     Example:
                |         The following example adds the iPoint frozen point to the
                |         hybShpCurveSmooth object.
                | 
                |          hybShpCurveSmooth.AddFrozenPoint iPoint
                |          
                | 
                | o Func GetFrozenCurveSegment(long iPos) As Reference
                | 
                |     Retrieves the Frozen Curve Segment at specified position in the hybrid
                |     shape curve smooth object.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the Frozen Curve Segment to retrieve.
                |             
                | 
                |     Example:
                |         The following example gets the oCurve Frozen Curve Segment of the
                |         hybShpCurveSmooth object at the position iPos.
                | 
                |          Dim oCurve As Reference
                |          Set oCurve = hybShpCurveSmooth.GetFrozenCurveSegment (iPos).
                |          
                | 
                | o Func GetFrozenCurveSegmentsSize() As long
                | 
                |     Returns the number of frozen curve segments in the curve smooth
                |     object.
                | 
                |     Parameters:
                | 
                |         oSize
                |             Number of frozen curve segments in the curve
                |             smooth.
                | 
                |             Example:
                |                 This example retrieves the number of frozen curve segments. in
                |                 the hybShpCurveSmooth hybrid shape curve
                |                 smooth.
                | 
                |                  Dim oSize As  long
                |                  oSize = hybShpCurveSmooth.GetFrozenCurveSegmentsSize
                |                  
                | 
                | o Func GetFrozenPoint(long iPos) As Reference
                | 
                |     Retrieves the Frozen Point at specified position in the hybrid shape curve
                |     smooth object.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the Frozen Point to retrieve. 
                | 
                |     Example:
                |         The following example gets the oPoint Frozen Point of the
                |         hybShpCurveSmooth object at the position iPos.
                | 
                |          Dim oPoint As Reference
                |          Set oPoint = hybShpCurveSmooth.GetFrozenPoint (iPos).
                |          
                | 
                | o Func GetFrozenPointsSize() As long
                | 
                |     Returns the number of Frozen Points in the curve smooth
                |     object.
                | 
                |     Parameters:
                | 
                |         oSize
                |             Number of Frozen Points in the curve smooth.
                | 
                |             Example:
                |                 This example retrieves the number of Frozen Points. in the
                |                 hybShpCurveSmooth hybrid shape curve smooth.
                | 
                |                  Dim oSize As  long
                |                  oSize = hybShpCurveSmooth.GetFrozenPointsSize
                |                  
                | 
                | o Sub RemoveAllFrozenCurveSegments()
                | 
                |     Removes all Frozen Curve Segment of the hybrid shape curve smooth object.
                |     
                | 
                | Example:
                |     The following example removes all Frozen Curve Segments of the
                |     hybShpCurveSmooth object.
                | 
                |      hybShpCurveSmooth.RemoveAllFrozenCurveSegments
                |      
                | 
                | o Sub RemoveAllFrozenPoints()
                | 
                |     Removes all Frozen Points of the hybrid shape curve smooth object.
                |     
                | 
                | Example:
                |     The following example removes all Frozen Points of the hybShpCurveSmooth
                |     object.
                | 
                |      hybShpCurveSmooth.RemoveAllFrozenPoints
                |      
                | 
                | o Sub RemoveFrozenCurveSegment(Reference iCurve)
                | 
                |     Removes Frozen Curve Segment from the list of Forzen curves in hybrid shape
                |     curve smooth object.
                | 
                |     Parameters:
                | 
                |         iCurve
                |             The Frozen Curve Segment to remove. 
                | 
                |     Example:
                |         The following example removes the Frozen Curve Segment from the
                |         hybShpCurveSmooth object.
                | 
                |          hybShpCurveSmooth.RemoveFrozenCurveSegment iCurve.
                |          
                | 
                | o Sub RemoveFrozenPoint(Reference iPoint)
                | 
                |     Removes Frozen Point from the list of frozen points in hybrid shape curve
                |     smooth object.
                | 
                |     Parameters:
                | 
                |         iPoint
                |             The Frozen Point to remove. 
                | 
                |     Example:
                |         The following example removes the Frozen Point from the
                |         hybShpCurveSmooth object.
                | 
                |          hybShpCurveSmooth.RemoveFrozenPoint iPoint.
                |          
                | 
                | o Sub SetMaximumDeviation(double iMaxDeviation)
                | 
                |     Sets the maximum deviation.
                | 
                |     Parameters:
                | 
                |         iMaxDeviation
                |             The maximium deviation
                | 
                | o Sub SetTangencyThreshold(double iTangencyThreshold)
                | 
                |     Sets the tangency threshold.
                | 
                |     Parameters:
                | 
                |         iTangencyThreshold
                |             The tangency threshold

        :return: bool
        """

        return self.hybrid_shape_curve_smooth.TopologySimplificationActivity

    @topology_simplification_activity.setter
    def topology_simplification_activity(self, value):
        """
        :param bool value:
        """

        self.hybrid_shape_curve_smooth.TopologySimplificationActivity = value

    def __repr__(self):
        return f'HybridShapeCurveSmooth(name="{ self.name }")'