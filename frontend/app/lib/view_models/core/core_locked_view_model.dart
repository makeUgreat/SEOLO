import 'package:app/models/core/locked_model.dart';
import 'package:app/services/core_service.dart';
import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class CoreLockedViewModel extends ChangeNotifier {
  final _storage = const FlutterSecureStorage();
  final CoreService _coreService = CoreService();
  CoreLockedModel? _coreLockedModel;
  String? lockerUid;
  String? battery;
  String? machineId;
  bool _isLoading = false;
  String? _errorMessage;

  bool get isLoading => _isLoading;

  String? get errorMessage => _errorMessage;

  Future<void> initializeData() async {
    lockerUid = await _storage.read(key: 'locker_uid');
    battery = await _storage.read(key: 'locker_battery');
    int? batteryInfo = (battery != null) ? int.parse(battery!) : 0;
    machineId = await _storage.read(key: 'machine_id');
    int? machineIdInfo = (machineId != null) ? int.parse(machineId!) : 0;
    _coreLockedModel = CoreLockedModel(
        lockerUid: lockerUid ?? '',
        battery: batteryInfo,
        machineId: machineIdInfo);
    notifyListeners();
  }

  Future<void> coreLocked() async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    await initializeData();

    final result = await _coreService.coreLocked(_coreLockedModel!);
    _isLoading = false;

    if (!result['success']) {
      _errorMessage = result['message'];
    } else {
      _errorMessage = null;
    }
    notifyListeners();
  }
}
