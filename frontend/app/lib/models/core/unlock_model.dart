class CoreUnlockModel {
  final String? lockerUid;
  final int? battery;
  final int? machineId;
  final String? tokenValue;

  CoreUnlockModel({
    this.lockerUid,
    this.battery,
    this.machineId,
    this.tokenValue,
  });

  Map<String, dynamic> toJson() => {
        'locker_uid': lockerUid,
        'battery_info': battery,
        'machine_id': machineId,
        'token_value': tokenValue,
      };
}
