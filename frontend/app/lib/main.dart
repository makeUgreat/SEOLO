import 'package:app/routes/main_route.dart';
import 'package:app/screens/login/login_screen.dart';
import 'package:app/view_models/core/core_check_view_model.dart';
import 'package:app/view_models/core/core_issue_view_model.dart';
import 'package:app/view_models/core/core_locked_view_model.dart';
import 'package:app/view_models/core/core_unlock_view_model.dart';
import 'package:app/view_models/loto/checklist_view_model.dart';
import 'package:app/view_models/loto/facility_view_model.dart';
import 'package:app/view_models/loto/machine_view_model.dart';
import 'package:app/view_models/loto/task_templates_view_model.dart';
import 'package:app/view_models/main/news_view_model.dart';
import 'package:app/view_models/user/login_view_model.dart';
import 'package:app/view_models/user/my_info_view_model.dart';
import 'package:app/view_models/user/my_tasks_view_model.dart';
import 'package:app/view_models/user/password_change_view_model.dart';
import 'package:app/view_models/user/password_check_view_model.dart';
import 'package:app/view_models/user/pin_change_view_model.dart';
import 'package:app/view_models/user/pin_login_view_model.dart';
import 'package:app/view_models/user/logout_view_model.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_blue_plus/flutter_blue_plus.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:provider/provider.dart';
import 'package:flutter_localizations/flutter_localizations.dart';

const Color blue100 = Color.fromRGBO(135, 185, 231, 1);
const Color blue400 = Color.fromRGBO(52, 107, 190, 1);
const Color blue800 = Color.fromRGBO(56, 61, 101, 1);
const Color mint200 = Color.fromRGBO(207, 241, 214, 1);
const Color gray100 = Color.fromRGBO(242, 244, 247, 1);
const Color gray200 = Color.fromRGBO(228, 231, 236, 1);
const Color gray800 = Color.fromRGBO(29, 41, 57, 1);
const Color samsungBlue = Color.fromRGBO(20, 40, 160, 1);
const Color safetyBlue = Color.fromRGBO(0, 0, 255, 1);
const Color snow = Color.fromRGBO(255, 250, 250, 1);
const Color green400 = Color.fromRGBO(93, 210, 122, 1);
const Color red300 = Color.fromRGBO(241, 38, 13, 1);
const Color yellow200 = Color.fromRGBO(250, 237, 11, 1);
const Color safetyRed = Color.fromRGBO(255, 0, 0, 1);
// 그림자
const BoxShadow shadow = BoxShadow(
  color: Color.fromRGBO(0, 0, 0, 0.25),
  blurRadius: 5,
  offset: Offset(0, 2),
);

void main() async {
  WidgetsFlutterBinding.ensureInitialized(); // 초기화 보장

  await dotenv.load(fileName: '.env');
  SystemChrome.setPreferredOrientations(
      [DeviceOrientation.portraitUp, DeviceOrientation.portraitDown]);
  runApp(
    const MyApp(),
  );
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (_) => NewsViewModel()),
          ChangeNotifierProvider(create: (_) => LoginViewModel()),
          ChangeNotifierProvider(create: (_) => LogoutViewModel()),
          ChangeNotifierProvider(create: (_) => PinLoginViewModel()),
          ChangeNotifierProvider(create: (_) => PinChangeViewModel()),
          ChangeNotifierProvider(create: (_) => MyInfoViewModel()),
          ChangeNotifierProvider(create: (_) => PasswordChangeViewModel()),
          ChangeNotifierProvider(create: (_) => PasswordCheckViewModel()),
          ChangeNotifierProvider(create: (_) => MyTasksViewModel()),
          ChangeNotifierProvider(create: (_) => CoreIssueViewModel()),
          ChangeNotifierProvider(create: (_) => ChecklistViewModel()),
          ChangeNotifierProvider(create: (_) => FacilityViewModel()),
          ChangeNotifierProvider(create: (_) => MachineViewModel()),
          ChangeNotifierProvider(create: (_) => TaskTemplatesViewModel()),
          ChangeNotifierProvider(create: (_) => CoreIssueViewModel()),
          ChangeNotifierProvider(create: (_) => CoreCheckViewModel()),
          ChangeNotifierProvider(create: (_) => CoreLockedViewModel()),
          ChangeNotifierProvider(create: (_) => CoreUnlockViewModel()),
        ],
        child: MaterialApp(
          localizationsDelegates: const [
            GlobalMaterialLocalizations.delegate,
            GlobalCupertinoLocalizations.delegate,
          ],
          supportedLocales: const [
            Locale('en', ''), // English, no country code
            Locale('ko', ''), // Korean, no country code
          ],
          title: 'SeoLo',
          theme: ThemeData(
              primarySwatch: Colors.blue,
              visualDensity: VisualDensity.adaptivePlatformDensity,
              fontFamily: 'font'),
          home: const SplashScreen(),
          onGenerateRoute: generateMainRoute,
        ));
  }
}

class SplashScreen extends StatelessWidget {
  final storage = const FlutterSecureStorage();

  const SplashScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: storage.read(key: 'token'),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return const CircularProgressIndicator();
        } else {
          if (snapshot.data != null) {
            WidgetsBinding.instance.addPostFrameCallback((_) {
              Navigator.pushReplacementNamed(context, '/pinLogin');
            });
          } else {
            WidgetsBinding.instance.addPostFrameCallback((_) {
              Navigator.pushReplacementNamed(context, '/login');
            });
          }
          return Container();
        }
      },
    );
  }
}
