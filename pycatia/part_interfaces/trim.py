#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.reference import Reference
from pycatia.part_interfaces.boolean_shape import BooleanShape


class Trim(BooleanShape):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.BooleanShape
                |                             Trim
                | 
                | Represents the Trim, or union trim boolean operation.
                | It is performed between a body and the current shape.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.trim = com_object

    def add_face_to_keep(self, i_face_to_keep: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddFaceToKeep(Reference iFaceToKeep)
                | 
                |     Adds a new face to be kept (if face is not divided by
                |     operation).
                | 
                |     Parameters:
                | 
                |         iFaceToKeep
                |             The new face to process
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                | 
                | Example:
                |     The following example adds the new face face to Keep for the Trim
                |     firstTrim:
                | 
                |      call firstTrim.AddFaceToKeep(face)

        :param Reference i_face_to_keep:
        :return: None
        :rtype: None
        """
        return self.trim.AddFaceToKeep(i_face_to_keep.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_face_to_keep'
        # # vba_code = """
        # # Public Function add_face_to_keep(trim)
        # #     Dim iFaceToKeep (2)
        # #     trim.AddFaceToKeep iFaceToKeep
        # #     add_face_to_keep = iFaceToKeep
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_face_to_keep2(self, i_face_to_keep: Reference, i_face_adjacent_for_keep: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddFaceToKeep2(Reference iFaceToKeep,
                | Reference iFaceAdjacentForKeep)
                | 
                |     Adds a new face to be kept (if face is divided by
                |     operation).
                | 
                |     Parameters:
                | 
                |         iFaceToKeep
                |             The new face to process
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                |     iFaceAdjacentForKeep
                |         An adjacent face of iFaceToKeep belonging to the other
                |         operand
                |         The following Boundary object is supported: Face.
                | 
                | Example:
                |     The following example adds the new face face to Keep for the Trim
                |     firstTrim:
                | 
                |      call firstTrim.AddFaceToKeep(face)

        :param Reference i_face_to_keep:
        :param Reference i_face_adjacent_for_keep:
        :return: None
        :rtype: None
        """
        return self.trim.AddFaceToKeep2(i_face_to_keep.com_object, i_face_adjacent_for_keep.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_face_to_keep2'
        # # vba_code = """
        # # Public Function add_face_to_keep2(trim)
        # #     Dim iFaceToKeep (2)
        # #     trim.AddFaceToKeep2 iFaceToKeep
        # #     add_face_to_keep2 = iFaceToKeep
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_face_to_remove(self, i_face_to_remove: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddFaceToRemove(Reference iFaceToRemove)
                | 
                |     Adds a new face to be Removed (if face not divided by
                |     operation).
                | 
                |     Parameters:
                | 
                |         iFaceToRemove
                |             The new face to process
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                | 
                | Example:
                |     The following example adds the new face face to Remove for the Trim
                |     firstTrim:
                | 
                |      call firstTrim.AddFaceToRemove(face)

        :param Reference i_face_to_remove:
        :return: None
        :rtype: None
        """
        return self.trim.AddFaceToRemove(i_face_to_remove.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_face_to_remove'
        # # vba_code = """
        # # Public Function add_face_to_remove(trim)
        # #     Dim iFaceToRemove (2)
        # #     trim.AddFaceToRemove iFaceToRemove
        # #     add_face_to_remove = iFaceToRemove
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_face_to_remove2(self, i_face_to_remove: Reference, i_face_adjacent_for_remove: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddFaceToRemove2(Reference iFaceToRemove,
                | Reference iFaceAdjacentForRemove)
                | 
                |     Adds a new face to be Removed (if face is divided by
                |     operation).
                | 
                |     Parameters:
                | 
                |         iFaceToRemove
                |             The new face to process
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                |     iFaceAdjacentForRemove
                |         An adjacent face of iFaceToRemove belonging to the other
                |         operand
                |         The following Boundary object is supported: Face.
                | 
                | Example:
                |     The following example adds the new face face to Remove for the Trim
                |     firstTrim:
                | 
                |      call firstTrim.AddFaceToRemove(face)

        :param Reference i_face_to_remove:
        :param Reference i_face_adjacent_for_remove:
        :return: None
        :rtype: None
        """
        return self.trim.AddFaceToRemove2(i_face_to_remove.com_object, i_face_adjacent_for_remove.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_face_to_remove2'
        # # vba_code = """
        # # Public Function add_face_to_remove2(trim)
        # #     Dim iFaceToRemove (2)
        # #     trim.AddFaceToRemove2 iFaceToRemove
        # #     add_face_to_remove2 = iFaceToRemove
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def withdraw_face_to_keep(self, i_face_to_withdraw: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub WithdrawFaceToKeep(Reference iFaceToWithdraw)
                | 
                |     Withdraws an existing Kept face (if face is not divided by operation)
                |     .
                | 
                |     Parameters:
                | 
                |         iFaceToWithdraw
                |             The face to withdraw
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                | 
                | Example:
                |     The following example withdraws the existing face Kept face from the Trim
                |     firstTrim:
                | 
                |      call firstTrim.WithdrawFaceToKeep(face)

        :param Reference i_face_to_withdraw:
        :return: None
        :rtype: None
        """
        return self.trim.WithdrawFaceToKeep(i_face_to_withdraw.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'withdraw_face_to_keep'
        # # vba_code = """
        # # Public Function withdraw_face_to_keep(trim)
        # #     Dim iFaceToWithdraw (2)
        # #     trim.WithdrawFaceToKeep iFaceToWithdraw
        # #     withdraw_face_to_keep = iFaceToWithdraw
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def withdraw_face_to_keep2(self, i_face_to_withdraw: Reference, i_face_adjacent_for_keep: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub WithdrawFaceToKeep2(Reference iFaceToWithdraw,
                | Reference iFaceAdjacentForKeep)
                | 
                |     Withdraws an existing Kept face (if face is divided by
                |     operation).
                | 
                |     Parameters:
                | 
                |         iFaceToWithdraw
                |             The face to withdraw
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                |     iFaceAdjacentForKeep
                |         An adjacent face of iFaceToKeep belonging to the other
                |         operand
                |         The following Boundary object is supported: Face.
                | 
                | Example:
                |     The following example withdraws the existing face Kept face from the Trim
                |     firstTrim:
                | 
                |      call firstTrim.WithdrawFaceToKeep(face)

        :param Reference i_face_to_withdraw:
        :param Reference i_face_adjacent_for_keep:
        :return: None
        :rtype: None
        """
        return self.trim.WithdrawFaceToKeep2(i_face_to_withdraw.com_object, i_face_adjacent_for_keep.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'withdraw_face_to_keep2'
        # # vba_code = """
        # # Public Function withdraw_face_to_keep2(trim)
        # #     Dim iFaceToWithdraw (2)
        # #     trim.WithdrawFaceToKeep2 iFaceToWithdraw
        # #     withdraw_face_to_keep2 = iFaceToWithdraw
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def withdraw_face_to_remove(self, i_face_to_withdraw: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub WithdrawFaceToRemove(Reference iFaceToWithdraw)
                | 
                |     Withdraws an existing Removed face (if face not divided by
                |     operation).
                | 
                |     Parameters:
                | 
                |         iFaceToWithdraw
                |             The face to withdraw
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                | 
                | Example:
                |     The following example withdraws the existing face Removed face from the
                |     Trim firstTrim:
                | 
                |      call firstTrim.WithdrawFaceToRemove(face)

        :param Reference i_face_to_withdraw:
        :return: None
        :rtype: None
        """
        return self.trim.WithdrawFaceToRemove(i_face_to_withdraw.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'withdraw_face_to_remove'
        # # vba_code = """
        # # Public Function withdraw_face_to_remove(trim)
        # #     Dim iFaceToWithdraw (2)
        # #     trim.WithdrawFaceToRemove iFaceToWithdraw
        # #     withdraw_face_to_remove = iFaceToWithdraw
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def withdraw_face_to_remove2(self, i_face_to_withdraw: Reference, i_face_adjacent_for_remove: Reference) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub WithdrawFaceToRemove2(Reference iFaceToWithdraw,
                | Reference iFaceAdjacentForRemove)
                | 
                |     Withdraws an existing Removed face (if face is divided by
                |     operation).
                | 
                |     Parameters:
                | 
                |         iFaceToWithdraw
                |             The face to withdraw
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                |     iFaceAdjacentForRemove
                |         An adjacent face of iFaceToRemove belonging to the other
                |         operand
                |         The following Boundary object is supported: Face.
                | 
                | Example:
                |     The following example withdraws the existing face Removed face from the
                |     Trim firstTrim:
                | 
                |      call firstTrim.WithdrawFaceToRemove(face)

        :param Reference i_face_to_withdraw:
        :param Reference i_face_adjacent_for_remove:
        :return: None
        :rtype: None
        """
        return self.trim.WithdrawFaceToRemove2(i_face_to_withdraw.com_object, i_face_adjacent_for_remove.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'withdraw_face_to_remove2'
        # # vba_code = """
        # # Public Function withdraw_face_to_remove2(trim)
        # #     Dim iFaceToWithdraw (2)
        # #     trim.WithdrawFaceToRemove2 iFaceToWithdraw
        # #     withdraw_face_to_remove2 = iFaceToWithdraw
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Trim(name="{self.name}")'
