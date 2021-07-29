import json


class JsonReader:
    def __init__(self, file_handler):
        self.json_data = json.load(file_handler)
        self.file_name = file_handler.name

    def __str__(self):
        return self.file_name

    def __repr__(self):
        return self.file_name

    def get_cp_devices(self):
        return [cp_entry.get('vn_cp_lid') for cp_entry in self.json_data.get('assets', {}).get('cp_entries')]

    def get_space_devices(self):
        return [sky_sensor.get('space_id') for sky_sensor in
                self.json_data.get('assets', {}).get('spaces')]

    def get_zone_ids(self):
        return [zone.get('zone_id') for zone in
                self.json_data.get('assets', {}).get('zones')]

    def get_vn_fanc(self):
        devices = []
        for cp_entry in self.json_data.get('assets', {}).get('cp_entries'):
            for fanc in cp_entry.get('fanc_entries'):
                devices.append(fanc.get('vn_fanc_lid'))
        return devices

    def get_vn_pdu(self):
        devices = []
        for cp_entry in self.json_data.get('assets', {}).get('cp_entries'):
            for fanc in cp_entry.get('pdu_entries'):
                devices.append(fanc.get('vn_pdu_lid'))
        return devices

    def get_cphe(self):
        devices = []
        for cp_entry in self.json_data.get('assets', {}).get('cp_entries'):
            for cphe in cp_entry.get('cphe_entries'):
                devices.append(cphe.get('vn_cphe_lid'))
        return devices

    def get_trunks(self):
        devices = []
        for cp_entry in self.json_data.get('assets', {}).get('cp_entries'):
            for cphe in cp_entry.get('cphe_entries'):
                for trunk in cphe.get('trunk_entries'):
                    devices.append(trunk.get('vn_trunk_lid'))
        return devices

    def get_nt(self):
        devices = []
        for cp_entry in self.json_data.get('assets', {}).get('cp_entries'):
            for cphe in cp_entry.get('cphe_entries'):
                for trunk in cphe.get('trunk_entries'):
                    for nt in trunk.get('nt_entries'):
                        devices.append(nt.get('vn_nt_lid'))
        return devices

    def get_igu(self):
        devices = []
        for cp_entry in self.json_data.get('assets', {}).get('cp_entries'):
            for cphe in cp_entry.get('cphe_entries'):
                for trunk in cphe.get('trunk_entries'):
                    for nt in trunk.get('nt_entries'):
                        for device in nt.get('devices'):
                            if device.get('vn_igu_lid'):
                                devices.append(device.get('vn_igu_lid'))
        return devices

    def get_mantis(self):
        devices = []
        for cp_entry in self.json_data.get('assets', {}).get('cp_entries'):
            for cphe in cp_entry.get('cphe_entries'):
                for trunk in cphe.get('trunk_entries'):
                    for nt in trunk.get('nt_entries'):
                        for device in nt.get('devices'):
                            if device.get('vn_fix_lid'):
                                devices.append(device.get('vn_fix_lid'))
        return devices

    def get_sky_sensors(self):
        return [sky_sensor.get('vn_sky_lid') for sky_sensor in
                self.json_data.get('assets', {}).get('sky_sensor')]

    def get_zones(self):
        return [zone for zone in self.json_data.get('assets').get('zones')]

    def get_igus(self):
        data = []
        for cp_entry in self.json_data.get('assets').get('cp_entries', []):
            for cphe_entry in cp_entry.get('cphe_entries', []):
                for trunk in cphe_entry.get('trunk_entries', []):
                    for nt_entrie in trunk.get('nt_entries', []):
                        for device in nt_entrie.get('devices', {}):
                            if device.get('type') == 'igu':
                                data.append(device)
        return data

    def get_devices(self):
        data = []
        for cp_entry in self.json_data.get('assets').get('cp_entries', []):
            for cphe_entry in cp_entry.get('cphe_entries', []):
                for trunk in cphe_entry.get('trunk_entries', []):
                    for nt_entrie in trunk.get('nt_entries', []):
                        for device in nt_entrie.get('devices', {}):
                            data.append(device)
        return data

    def get_nwc_igus(self):
        data = []
        for cp_entry in self.json_data.get('assets').get('cp_entries', []):
            for cphe_entry in cp_entry.get('cphe_entries', []):
                for trunk in cphe_entry.get('trunk_entries', []):
                    for nt_entrie in trunk.get('nt_entries', []):
                        if nt_entrie.get('vn_nt_type') == 'nwc':
                            devices = [device for device in nt_entrie.get('devices') if device.get('type')]
                            data.append(devices)
        return data

    def get_project_id(self):
        return self.json_data.get('context', {}).get('projectId')
