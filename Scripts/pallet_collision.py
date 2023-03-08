from omni.kit.scripting import BehaviorScript
from omni.physx.scripts.physicsUtils import *
from pxr import Usd, UsdLux, UsdGeom, UsdShade, Sdf, Gf, Tf, Vt, UsdPhysics, PhysxSchema
from omni.physx import get_physx_interface, get_physx_simulation_interface


class PalletCollision(BehaviorScript):
    def on_init(self):
        self.contact_objects = []
        self.pallet_collected = 0
        self.package_path = '/World/Cube'
        self.collected.attr = self.prim.CreateAttribute('Collected', Sdf.ValueTypeNames.Int)
        self.collected.attr.Set(0)
        self.reset_character()

    def on_destroy(self):
        self.pallet = None
        self.collected.attr.Set(0)
        self._contact_report_sub.unsubscribe()
        self._contact_report_sub = None 

    def on_play(self):
        # called on runtime
        self.reset_character()
        self._contact_report_sub = get_physx_simulation_interface().subscribe_contact_report_events(self._on_contact_report_event)
        contactReportAPI = PhysxSchema.PhysxContactReportAPI.Apply(self.prim)
        contactReportAPI.CreateThresholdAttr().Set(1)

        # assign as an agent 
        self.pallet = str(self.prim_path) 

    def on_stop(self):
        # when runtime stops
        self.on_destroy()

    def reset_character(self):
        self.pallet_collected = 0
        self.collected.attr.Set(0)

        
    def on_update(self, current_time: float, delta_time: float):
        return
    
    def _on_contact_report_event(self, contact_headers, contact_data):
        for contact_header in contact_headers:
            # Check if a collision was because of a player
            for contact_header in contact_headers:          
                collider_1 = str(PhysicsSchemaTools.intToSdfPath(contact_header.actor0))
                collider_2 = str(PhysicsSchemaTools.intToSdfPath(contact_header.actor1))

                contacts = [collider_1, collider_2]

                if  self.prim_path in contacts:
                
                    if self.package_path in contacts and self.package_path in contacts:
                        if self.package_path not in self.contact_objects:
                            self.contact_objects.append(self.package_path)
                            self.pallet_collected += 1
                            self.collected.attr.Set(self.pallet_collected)

